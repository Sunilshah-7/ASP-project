<template>
  <div class="flex flex-col overflow-hidden">
    <header class="ml-8 max-md:ml-2.5">
      <img
        loading="lazy"
        src="@/assets/home-logo.png"
        alt="AI Assistant Logo"
        class="object-contain max-w-full aspect-[1.52] w-[156px]"
      />
    </header>
    <div class="bg-violet-400 h-[100vw] w-[100%]">
      <main class="flex flex-row justify-between mx-8 my-4">
        <div class="w-3/5 video-container">
          <iframe
            v-if="videoUrl"
            :src="`https://www.youtube.com/embed/${videoUrl}`"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
          ></iframe>
        </div>
        <div class="w-2/5 ml-4 tabs-container">
          <Tabs>
            <TabsList>
              <TabsTrigger value="tab1">Transcript</TabsTrigger>
              <TabsTrigger value="tab2">Summary</TabsTrigger>
              <TabsTrigger value="tab3">Quizzes</TabsTrigger>
            </TabsList>
            <TabsContent value="tab1">
              <p v-if="loadingTab1">Loading content...</p>
              <div v-else class="transcript-container">
                <table v-if="transcripts.length > 0" border="1">
                  <thead>
                    <tr>
                      <th>Start Time</th>
                      <th>End Time</th>
                      <th>Text</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(transcript, index) in transcripts" :key="index">
                      <td>{{ transcript.line_start }}</td>
                      <td>{{ transcript.line_end }}</td>
                      <td>{{ transcript.line_text }}</td>
                    </tr>
                  </tbody>
                </table>
                <p v-else>No transcript content available.</p>
              </div>
            </TabsContent>
            <TabsContent value="tab2">
              <p v-if="loadingTab2">Loading summary content...</p>
              <div v-else class="summary-container">
                <Card v-for="(topic, index) in summary" :key="index">
                  <CardHeader>
                    <CardTitle>{{ topic.main_topic }}</CardTitle>
                    <CardDescription>
                      <strong>Time Range:</strong> {{ topic.time_start }} -
                      {{ topic.time_end }}
                    </CardDescription>
                  </CardHeader>
                  <CardContent>
                    <img
                      :src="'data:image/jpeg;base64,' + topic.key_frame_img"
                      alt="Key Frame Image"
                    />
                    <ul>
                      <li
                        v-for="(subtopic, subIndex) in topic.subtopics"
                        :key="subIndex"
                      >
                        {{ subtopic }}
                      </li>
                    </ul>
                  </CardContent>
                </Card>
              </div>
            </TabsContent>
            <TabsContent value="tab3">
              <div v-if="loadingTab3">
                <p>Loading quizzes...</p>
              </div>
              <div v-else>
                <div
                  v-if="currentQuizIndex < quizzes.length"
                  class="quiz-container"
                >
                  <div class="question">
                    <strong
                      >Question {{ currentQuizIndex + 1 }} /
                      {{ quizzes.length }}:</strong
                    >
                    {{ quizzes[currentQuizIndex].question }}
                  </div>
                  <div class="options">
                    <label>
                      <input
                        type="radio"
                        name="quiz"
                        value="True"
                        v-model="selectedAnswer"
                      />
                      True
                    </label>
                    <label>
                      <input
                        type="radio"
                        name="quiz"
                        value="False"
                        v-model="selectedAnswer"
                      />
                      False
                    </label>
                  </div>
                  <button class="quiz-button" @click="submitAnswer">
                    Submit
                  </button>
                  <div class="feedback" v-if="feedback">
                    {{ feedback }}
                  </div>
                </div>
                <div v-else>
                  <h2>Quiz Completed!</h2>
                  <p>
                    You answered {{ correctAnswers }} /
                    {{ quizzes.length }} correctly.
                  </p>
                  <button class="quiz-button" @click="restartQuiz">
                    Restart Quiz
                  </button>
                </div>
              </div>
            </TabsContent>
          </Tabs>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { getTranscript, getSummary, getQuiz } from "@/api/request";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";

export default {
  name: "SummaryPage",
  props: {
    videoUrl: {
      type: String,
      required: true,
    },
  },
  components: {
    Tabs,
    TabsContent,
    TabsList,
    TabsTrigger,
    Card,
    CardContent,
    CardDescription,
    CardHeader,
    CardTitle,
  },
  data() {
    return {
      transcripts: [], // Transcript data
      summary: [], // Summary data
      quizzes: [], // Quiz data
      currentQuizIndex: 0, // Current quiz index
      correctAnswers: 0, // Correct answers count
      feedback: "", // Quiz feedback
      loadingTab1: true, // Loading status for Transcript
      loadingTab2: true, // Loading status for Summary
      loadingTab3: true, // Loading status for Quizzes
      selectedAnswer: "", // Selected answer for the quiz
    };
  },
  methods: {
    formatTime(timeInSeconds) {
      const hours = Math.floor(timeInSeconds / 3600);
      const minutes = Math.floor((timeInSeconds % 3600) / 60);
      const seconds = Math.floor(timeInSeconds % 60);
      //If the hour is 0, only minutes and seconds are displayed, otherwise the full time is displayed
      if (hours > 0) {
        return `${hours.toString().padStart(2, "0")}:${minutes
          .toString()
          .padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;
      }
      return `${minutes.toString().padStart(2, "0")}:${seconds
        .toString()
        .padStart(2, "0")}`;
    },
    async fetchTranscript() {
      this.loadingTab1 = true;
      try {
        const response = await getTranscript();

        // Map raw transcript data and format te
        this.transcripts = response.map((transcript) => ({
          ...transcript,
          line_start: this.formatTime(parseFloat(transcript.line_start)),
          line_end: this.formatTime(parseFloat(transcript.line_end)),
        }));
        console.log("Formatted transcript data:", this.transcripts);
      } catch (error) {
        console.error("Error fetching transcript:", error);
        toast.error("Failed to load transcript content.");
      } finally {
        this.loadingTab1 = false;
      }
    },
    async fetchSummary() {
      this.loadingTab2 = true;
      try {
        const response = await getSummary();
        // this.summary = response;
        this.summary = response.map((topic) => ({
          ...topic,
          time_start: this.formatTime(parseFloat(topic.time_start)),
          time_end: this.formatTime(parseFloat(topic.time_end)),
        }));
        console.log("Summary data:", this.summary);
      } catch (error) {
        console.error("Error fetching summary:", error);
        toast.error("Failed to load summary content.");
      } finally {
        this.loadingTab2 = false;
      }
    },
    async fetchQuizzes() {
      this.loadingTab3 = true;
      try {
        const response = await getQuiz();
        this.quizzes = response;
        console.log("Quiz data:", this.quizzes);
      } catch (error) {
        console.error("Error fetching quizzes:", error);
        toast.error("Failed to load quizzes.");
      } finally {
        this.loadingTab3 = false;
      }
    },
    submitAnswer() {
      if (
        this.selectedAnswer ===
        this.quizzes[this.currentQuizIndex].correct_answer
      ) {
        this.correctAnswers++;
        toast.success("Correct!", {
          position: "top-right",
          autoClose: 3000,
          hideProgressBar: false,
          closeOnClick: true,
          pauseOnHover: true,
          draggable: true,
          progress: undefined,
        });
      } else {
        toast.error(
          "Wrong! The correct answer is " +
            this.quizzes[this.currentQuizIndex].correct_answer +
            ".",
          {
            position: "top-right",
            autoClose: 3000,
            hideProgressBar: false,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
            progress: undefined,
          }
        );
      }
      setTimeout(() => {
        this.currentQuizIndex++;
        this.selectedAnswer = ""; // Reset the selected answer
      }, 1000);
    },
    restartQuiz() {
      this.currentQuizIndex = 0;
      this.correctAnswers = 0;
      this.feedback = "";
      this.selectedAnswer = ""; // Reset the selected answer
    },
  },
  async mounted() {
    try {
      await this.fetchTranscript();
      await this.fetchSummary();
      await this.fetchQuizzes();
    } catch (error) {
      console.error("Error during data fetching:", error);
    }
  },
};
</script>

<style scoped>
main {
  height: 70vh;
}
.video-container {
  height: 100%;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 1);
  background-color: #fff;
}
iframe {
  width: 100%;
  height: 100%;
  border: none;
}
.tabs-container {
  height: 100%;
  padding: 10px;
  border-radius: 8px;
  background-color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 1);
}
.transcript-container,
.summary-container {
  max-height: 550px; /* Set a maximum height */
  overflow-y: auto; /* Enable vertical scrolling */
  padding: 10px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
}
.transcript-container::-webkit-scrollbar,
.summary-container::-webkit-scrollbar {
  width: 8px;
}
.transcript-container::-webkit-scrollbar-thumb,
.summary-container::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 8px;
}
.transcript-container::-webkit-scrollbar-thumb:hover,
.summary-container::-webkit-scrollbar-thumb:hover {
  background: #555;
}
.quiz-container .question {
  font-size: 18px;
  margin-bottom: 10px;
}
.options label {
  display: block;
  margin: 10px 0;
  padding: 10px;
  font-size: 16px;
  cursor: pointer;
}
.quiz-button {
  display: block;
  margin: 10px 0;
  padding: 10px 20px;
  font-size: 16px;
  color: white;
  background-color: #4f46e5; /* Indigo background */
  border: none;
  border-radius: 8px;
  cursor: pointer;
  text-align: center;
}
.quiz-button:hover {
  background-color: #4338ca; /* Darker indigo on hover */
}
.feedback {
  margin-top: 10px;
  font-size: 16px;
  color: green;
}
</style>
