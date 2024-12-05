import numpy as np
import cv2
import os


def process_video_pipeline(video_path, start_time, end_time, output_video_path, frame_output_dir,
                           longest_still_frame_path, change_threshold=0.3, noise_tolerance=2):
    os.makedirs(frame_output_dir, exist_ok=True)  # Create frame output directory if not exists

    # Step 1: Extract video clip and save the first frame
    def extract_video_clip(video_path, start_time, end_time, output_path):
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        start_frame = int(start_time * fps)
        end_frame = int(end_time * fps)
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

        first_frame_path = os.path.join(frame_output_dir, "first_frame.jpg")
        frame_idx = start_frame
        first_frame_saved = False

        while cap.isOpened() and frame_idx <= end_frame:
            ret, frame = cap.read()
            if not ret:
                break
            if not first_frame_saved:
                cv2.imwrite(first_frame_path, frame)
                first_frame_saved = True
            out.write(frame)
            frame_idx += 1

        cap.release()
        out.release()
        print(f"Clip saved to {output_path} and first frame saved to {first_frame_path}")
        return first_frame_path

    # Step 2: Detect slide area using a histogram-based dynamic threshold
    def detect_and_isolate_slide_area(image_path):
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError("Unable to read image. Please check the file path.")

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Calculate histogram and analyze the proportion of white pixels
        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
        total_pixels = np.sum(hist)
        white_pixels = np.sum(hist[220:])  # Count pixels in the 220-255 range
        white_ratio = white_pixels / total_pixels

        # Determine threshold dynamically based on the white pixel ratio
        if white_ratio > 0.4:
            threshold_value = 250
        elif white_ratio > 0.3:
            threshold_value = 230
        elif white_ratio > 0.1:
            threshold_value = 220
        else:
            threshold_value = 210

        # Apply thresholding with the chosen value
        _, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

        # Find connected regions (contours)
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            raise ValueError("No contours found in the image.")

        # Identify the largest connected region
        largest_contour = max(contours, key=cv2.contourArea)

        # Create a mask for the largest region
        mask = np.zeros_like(gray)
        cv2.drawContours(mask, [largest_contour], -1, 255, thickness=cv2.FILLED)

        # Calculate the bounding rectangle of the region
        x, y, w, h = cv2.boundingRect(largest_contour)

        # Save the detected slide area for visualization (optional)
        isolated_slide = image[y:y + h, x:x + w]
        cv2.imwrite("detected_slide_area_histogram.png", isolated_slide)

        print(f"White pixel ratio: {white_ratio:.2f}, Adaptive threshold: {threshold_value}")
        return mask, (x, y, w, h)

    # Step 3: Process video and create slide matrix
    def process_video(video_path, mask, bbox, frame_output_dir):
        cap = cv2.VideoCapture(video_path)
        x, y, w, h = bbox
        slide_matrix = []
        frame_idx = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if frame_idx % 10 == 0:
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                slide_area = gray_frame[y:y + h, x:x + w]
                slide_matrix.append(slide_area)
#                cv2.imwrite(os.path.join(frame_output_dir, f"frame_{frame_idx}.png"), slide_area)
            frame_idx += 1

        cap.release()
        return np.stack(slide_matrix, axis=-1)

    # Step 4: Detect pixel changes with sliding window
    def detect_pixel_changes(slide_matrix, change_threshold=0.3, noise_tolerance=2):
        _, _, num_frames = slide_matrix.shape
        change_flags = np.zeros(num_frames, dtype=np.int32)

        for frame_idx in range(1, num_frames):
            diff = np.abs(slide_matrix[:, :, frame_idx] - slide_matrix[:, :, frame_idx - 1])
            change_ratio = np.sum(diff > 0) / diff.size
            change_flags[frame_idx] = 1 if change_ratio > change_threshold else 0

        # Reduce noise by eliminating isolated change frames
        for frame_idx in range(1, num_frames - 1):
            if change_flags[frame_idx] == 1:
                if (change_flags[frame_idx - 1] == 0 and change_flags[frame_idx + 1] == 0):
                    if noise_tolerance >= 2:
                        change_flags[frame_idx] = 0

        return change_flags

    # Step 5: Analyze and save results
    def analyze_and_save(slide_matrix, change_flags, longest_still_frame_path):
        longest_still_period = 0
        longest_start_frame = 0
        current_still_period = 0
        current_start_frame = 0

        for i, flag in enumerate(change_flags):
            if flag == 0:
                if current_still_period == 0:
                    current_start_frame = i
                current_still_period += 1
                if current_still_period > longest_still_period:
                    longest_still_period = current_still_period
                    longest_start_frame = current_start_frame
            else:
                current_still_period = 0

        print(
            f"The frame with the longest still period starts at frame {longest_start_frame} and lasts for {longest_still_period} frames.")
        if longest_start_frame < slide_matrix.shape[2]:
            longest_still_frame = slide_matrix[:, :, longest_start_frame]
            cv2.imwrite(longest_still_frame_path, longest_still_frame)
            print(f"Longest still frame saved to {longest_still_frame_path}")

    # Run pipeline steps
    first_frame_path = extract_video_clip(video_path, start_time, end_time, output_video_path)
    mask, bbox = detect_and_isolate_slide_area(first_frame_path)
    slide_matrix = process_video(output_video_path, mask, bbox, frame_output_dir)
    change_flags = detect_pixel_changes(slide_matrix, change_threshold, noise_tolerance)
    analyze_and_save(slide_matrix, change_flags, longest_still_frame_path)


# Example usage
process_video_pipeline(
    video_path=r'D:\coding practice\test.mp4',
    start_time=10,
    end_time=15,
    output_video_path=r'D:\coding practice\test_cut.mp4',
    frame_output_dir=r'D:\coding practice\frames',
    longest_still_frame_path=r'D:\coding practice\longest_still_frame.png',
    change_threshold=0.1,
    noise_tolerance=2
)
