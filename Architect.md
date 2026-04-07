# Architect.md

# AI-Assisted Learning App for Educational YouTube Videos

## 1. Project Overview

This project is a full-stack AI learning platform that transforms passive YouTube video watching into an active learning experience. The system accepts an educational YouTube video URL, extracts the audio, transcribes the speech with timestamps using Whisper, processes the transcript into summaries and quizzes, and presents an interactive study workflow through a Vue frontend.

The expanded version of the project is designed to demonstrate strong full-stack engineering skills using a recruiter-friendly stack:

- **Frontend:** Vue 3, Vite, Vue Router, Pinia, Tailwind CSS
- **Backend:** Java Spring Boot
- **AI/Transcription Service:** Python + FastAPI + Whisper
- **Database:** PostgreSQL
- **Caching / Async Messaging:** Redis
- **Containerization:** Docker + Docker Compose
- **Optional Realtime Updates:** Server-Sent Events (SSE) or WebSocket
- **Deployment:** Linux-based server, Dockerized services, reverse proxy with Nginx

This is not just a transcript app. It is an educational product with timestamp-aware study tools, quiz generation, progress tracking, and a reusable service-oriented architecture.

---

## 2. Core Product Goal

The main goal is to help users actively learn from educational YouTube videos by converting long-form video content into:

1. **Timestamped transcripts**
2. **Section-wise summaries**
3. **Quiz questions mapped to exact video moments**
4. **Progress tracking and review workflow**
5. **Interactive playback tied to learning content**

The user should be able to:

- paste a YouTube link
- process the video
- view transcript chunks with time anchors
- read AI-generated summaries by topic or segment
- take quizzes based on specific parts of the video
- click a summary or quiz explanation and jump directly to the relevant moment in the video
- revisit weak areas later

---

## 3. High-Level Functional Requirements

### 3.1 User-Facing Features

#### Video ingestion
- User submits a YouTube URL
- App validates the URL
- App extracts metadata such as title, duration, channel, thumbnail
- App starts a processing job

#### Audio transcription
- App downloads or extracts the audio track from the video
- Whisper transcribes the audio
- Transcript is returned with timestamps

#### Transcript experience
- Display transcript in chunks
- Allow click-to-seek behavior using timestamps
- Highlight the current transcript section while video plays

#### Summary generation
- Generate short summaries for each time block or topic block
- Allow users to expand detailed summaries
- Allow users to jump to the exact time segment

#### Quiz generation
- Generate MCQ, true/false, or short-answer questions
- Tie each question to one or more transcript segments
- Provide feedback and explanation
- Redirect the user to the relevant timestamp when they answer incorrectly

#### Learning analytics
- Track processed videos
- Track quiz scores
- Track topic weakness by section
- Store study sessions and completion states

#### Realtime status
- Show processing stages such as:
  - queued
  - downloading audio
  - transcribing
  - generating summaries
  - generating quiz
  - completed
  - failed

### 3.2 Admin / Engineering Features
- Logs for job lifecycle
- Error handling and retry support
- Health checks for each service
- API documentation
- Dockerized local development
- Environment-based configuration

---

## 4. Non-Functional Requirements

### Performance
- Video submission should return quickly after creating a job
- Long processing steps must happen asynchronously
- Transcript retrieval should be fast after processing completes

### Scalability
- Components should be split by responsibility
- Whisper should run as a separate service for independent scaling
- Job processing should be queue-friendly

### Reliability
- Every job should have a state machine
- Failures should be logged with reason
- Retrying a failed step should be possible

### Maintainability
- Backend should be layered clearly
- Frontend should use reusable components
- All configuration should be externalized

### Security
- Input validation for URLs
- Secure handling of uploaded / temporary files
- Authentication for user-specific features
- Rate limits for processing-heavy endpoints
- Sanitization of rendered content

### Usability
- Processing progress must be visible
- Video-linked summaries must be intuitive
- Quiz feedback should be educational and actionable

---

## 5. Architecture Overview

The cleanest design is a service-oriented architecture with clear separation of concerns.

### 5.1 Main Services

#### 1. Vue Frontend
Responsible for:
- rendering the UI
- submitting YouTube links
- showing processing status
- displaying transcript, summaries, quizzes, and progress
- interacting with the embedded YouTube player

#### 2. Spring Boot Backend
Responsible for:
- API orchestration
- user management
- video job creation and tracking
- persistence to PostgreSQL
- calling downstream services
- serving processed transcript and quiz content
- managing business logic and security

#### 3. Whisper Microservice
Responsible for:
- receiving audio file path or upload reference
- running Whisper transcription
- returning timestamped transcript JSON

#### 4. PostgreSQL
Stores:
- users
- videos
- processing jobs
- transcript segments
- summaries
- quizzes
- attempts
- progress

#### 5. Redis
Used for:
- queue metadata
- caching
- async job coordination
- temporary status data if needed

### 5.2 Recommended Flow

1. User submits YouTube URL from Vue
2. Spring validates URL and creates `video` and `job` records
3. Background processing starts
4. Audio is extracted/downloaded
5. Audio is sent to Whisper service
6. Whisper returns transcript with timestamps
7. Spring stores transcript segments
8. Summary generation runs
9. Quiz generation runs
10. Job marked complete
11. Vue shows transcript, summaries, and quiz

---

## 6. Suggested Tech Stack

## Frontend
- Vue 3
- Vite
- Vue Router
- Pinia
- Tailwind CSS
- Axios or Fetch API
- Video player integration with YouTube iframe API

## Backend
- Java 17 or 21
- Spring Boot 3.x
- Spring Web
- Spring Data JPA
- Spring Validation
- Spring Security
- Spring Actuator
- Spring Scheduler or async processing support
- Lombok
- MapStruct optionally

## AI / Transcription Service
- Python 3.11+
- FastAPI
- Uvicorn
- OpenAI Whisper or faster-whisper
- ffmpeg
- pydantic

## Data Layer
- PostgreSQL
- Redis

## Infra / DevOps
- Docker
- Docker Compose
- Nginx
- Linux server
- GitHub Actions optionally for CI/CD

---

## 7. Why This Stack Makes Sense

### Vue 3
Vue is ideal for a responsive single-page app with reusable UI components. It is lightweight, modern, and very suitable for transcript panels, learning dashboards, and quiz flows.

### Spring Boot
Spring Boot is ideal for this resume-targeted version because it gives strong backend credibility. It supports clean REST API development, validation, security, database integration, and production-style engineering patterns.

### Whisper in Python
Whisper’s native ecosystem is Python-first. Running it as a separate microservice keeps the Java backend clean and avoids trying to force model execution into Java. This also makes future replacement with another transcription model easier.

### PostgreSQL
The data is relational and structured: users, videos, jobs, transcript chunks, summaries, quizzes, and attempts. PostgreSQL also supports JSONB when semi-structured fields are helpful.

### Redis
Useful for async coordination, caching, or storing transient processing status.

---

## 8. Core Domain Model

The following entities are recommended.

### User
Stores account-level information.

Fields:
- id
- name
- email
- password_hash or oauth_identifier
- created_at
- updated_at

### Video
Represents a submitted YouTube video.

Fields:
- id
- user_id
- youtube_url
- youtube_video_id
- title
- description
- channel_name
- thumbnail_url
- duration_seconds
- language
- processing_status
- created_at
- updated_at

### ProcessingJob
Tracks the asynchronous pipeline.

Fields:
- id
- video_id
- status
- stage
- error_message
- started_at
- completed_at
- retry_count

### Transcript
Top-level transcript metadata.

Fields:
- id
- video_id
- full_text
- language
- source_model
- created_at

### TranscriptSegment
Stores timestamped speech chunks.

Fields:
- id
- transcript_id
- start_seconds
- end_seconds
- text
- segment_index
- topic_label optional

### Summary
Stores AI-generated summary units.

Fields:
- id
- video_id
- transcript_segment_start_index
- transcript_segment_end_index
- start_seconds
- end_seconds
- title
- summary_text
- created_at

### Quiz
Represents a generated quiz for a video.

Fields:
- id
- video_id
- title
- difficulty
- created_at

### QuizQuestion
Fields:
- id
- quiz_id
- question_text
- question_type
- options_json
- correct_answer
- explanation
- start_seconds
- end_seconds
- transcript_reference

### QuizAttempt
Fields:
- id
- quiz_id
- user_id
- score
- submitted_at

### QuizAnswer
Fields:
- id
- quiz_attempt_id
- question_id
- selected_answer
- is_correct

### StudyProgress
Tracks learning state.

Fields:
- id
- user_id
- video_id
- completion_percent
- weak_topics_json
- last_accessed_at

---

## 9. System Modules

## 9.1 Frontend Modules

### Authentication module
- login
- signup
- session management

### Video submission module
- paste link form
- validation
- submit request
- processing status display

### Study view module
- video player
- transcript panel
- summaries panel
- click-to-seek interactions

### Quiz module
- question rendering
- answer submission
- score feedback
- jump-to-explanation timestamp

### Dashboard module
- processed videos
- quiz scores
- progress history
- weak topic summaries

## 9.2 Backend Modules

### Auth module
- registration
- login
- JWT or session auth

### Video ingestion module
- validate URL
- parse YouTube ID
- save metadata
- create processing job

### Job orchestration module
- enqueue processing pipeline
- update job status by stage
- handle failures and retries

### Transcript module
- store transcript
- store transcript segments
- retrieve transcript by video

### Summary module
- generate and store summaries
- return grouped summaries

### Quiz module
- generate quiz
- persist questions
- evaluate answers
- store quiz attempts

### Progress module
- compute weak areas
- persist learning metrics

### Notification or status module
- send job status updates using SSE or WebSocket

## 9.3 AI Service Modules

### Audio transcription endpoint
- accept input file or path
- invoke Whisper
- return segment-based transcript

### Optional text-processing endpoints
If you later want to move text summarization or quiz generation into Python, this can be added as separate endpoints.

---

## 10. API Design

Below is a recommended first version of REST endpoints.

## Authentication
- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET /api/auth/me`

## Videos
- `POST /api/videos/process`
- `GET /api/videos`
- `GET /api/videos/{videoId}`
- `DELETE /api/videos/{videoId}`

## Jobs
- `GET /api/jobs/{jobId}`
- `GET /api/jobs/{jobId}/status`

## Transcript
- `GET /api/videos/{videoId}/transcript`
- `GET /api/videos/{videoId}/segments`

## Summaries
- `GET /api/videos/{videoId}/summaries`

## Quizzes
- `POST /api/videos/{videoId}/quiz/generate`
- `GET /api/videos/{videoId}/quiz`
- `POST /api/quizzes/{quizId}/submit`
- `GET /api/quizzes/{quizId}/results/{attemptId}`

## Progress
- `GET /api/users/me/progress`
- `GET /api/videos/{videoId}/progress`

## Realtime / Status
- `GET /api/jobs/{jobId}/stream` for SSE
or
- `/ws/jobs/{jobId}` for WebSocket

---

## 11. Data Flow in Detail

## Step 1: User submits video URL
Frontend sends a request to:

`POST /api/videos/process`

Payload example:
```json
{
  "youtubeUrl": "https://www.youtube.com/watch?v=abc123"
}
```

Spring performs:
- URL validation
- extraction of video ID
- metadata fetch if needed
- creates `video` row
- creates `processing_job` row
- returns `videoId` and `jobId`

## Step 2: Start async job
Backend should not block the request. Instead:
- queue job
- begin background execution
- set job stage to `DOWNLOADING_AUDIO`

## Step 3: Download / extract audio
A processing worker downloads the audio stream using a safe tool or service. The audio is saved temporarily.

## Step 4: Send to Whisper service
Spring sends the file path or file stream to the Python service.

Example endpoint:
`POST /transcribe`

Whisper returns:
```json
{
  "language": "en",
  "full_text": "...",
  "segments": [
    {
      "start": 0.0,
      "end": 12.7,
      "text": "Welcome to today's lecture"
    }
  ]
}
```

## Step 5: Store transcript
Spring stores:
- transcript metadata
- segment rows

## Step 6: Generate summaries
Summaries can be created from grouped segments. Recommended initial approach:
- group every 2 to 5 minutes or by N segments
- create one summary per chunk
- optionally label chunks with a generated title

## Step 7: Generate quiz
Quiz generation should take a subset or the full transcript and produce:
- question
- options
- correct answer
- explanation
- timestamp reference

## Step 8: Mark complete
Job status becomes `COMPLETED` and frontend can load the study interface.

---

## 12. Recommended Processing Strategy

## Version 1 strategy
Keep the first implementation simple.

### Transcript segmentation
- use Whisper segment output directly
- do not over-optimize chunking yet

### Summary segmentation
- group transcript segments into time windows of 2 to 5 minutes

### Quiz generation
- generate 5 to 10 questions based on summary windows

### Status tracking
- use a simple enum-based state machine

### Error handling
- one retry for transient failures
- permanent fail for invalid videos or broken processing

## Version 2 improvements
- topic-aware segmentation
- semantic transcript search
- adaptive quizzes based on weak topics
- spaced repetition reminders

---

## 13. Suggested Processing States

Use enums for consistency.

### JobStatus
- PENDING
- RUNNING
- COMPLETED
- FAILED

### JobStage
- CREATED
- VALIDATING_URL
- FETCHING_METADATA
- DOWNLOADING_AUDIO
- TRANSCRIBING_AUDIO
- STORING_TRANSCRIPT
- GENERATING_SUMMARIES
- GENERATING_QUIZ
- FINALIZING
- DONE
- ERROR

---

## 14. Database Design Guidance

A normalized relational schema is recommended.

### Tables
- users
- videos
- processing_jobs
- transcripts
- transcript_segments
- summaries
- quizzes
- quiz_questions
- quiz_attempts
- quiz_answers
- study_progress

### Important indexes
- `videos(user_id)`
- `processing_jobs(video_id)`
- `transcript_segments(transcript_id, segment_index)`
- `summaries(video_id)`
- `quiz_questions(quiz_id)`
- `study_progress(user_id, video_id)`

### Optional JSONB usage
- quiz options
- weak topics
- extra metadata

---

## 15. Frontend Design Requirements

## Main Pages

### 1. Landing / Dashboard Page
Contains:
- list of previously processed videos
- button to process new video
- recent learning activity

### 2. Process Video Page
Contains:
- input box for YouTube URL
- validation message
- submit button
- processing tracker

### 3. Study Page
Contains:
- embedded YouTube player
- transcript sidebar
- summary panel
- quiz entry point
- progress bar

### 4. Quiz Page
Contains:
- quiz instructions
- question-by-question flow
- results screen
- review by timestamp

## Reusable Components
- `AppHeader.vue`
- `VideoUrlForm.vue`
- `ProcessingStatusCard.vue`
- `VideoPlayer.vue`
- `TranscriptList.vue`
- `TranscriptSegmentItem.vue`
- `SummaryCard.vue`
- `QuizPanel.vue`
- `QuestionCard.vue`
- `ProgressStats.vue`
- `LoadingState.vue`
- `ErrorState.vue`

## UX Requirements
- clear loading indicators
- responsive layout
- easy click-to-seek from summary/transcript/question explanation
- educational feedback rather than generic correctness labels

---

## 16. Backend Design Requirements

Use standard layered architecture.

### Layers
- controller
- service
- repository
- dto
- mapper
- entity
- config
- exception
- security

### Good practices
- keep controllers thin
- put business logic into services
- validate input at the DTO layer
- use global exception handling
- keep external service calls abstracted through clients

### Example module boundaries
- `auth`
- `video`
- `job`
- `transcript`
- `summary`
- `quiz`
- `progress`
- `common`

---

## 17. AI / Whisper Service Design

## Responsibilities
- accept audio file
- run transcription
- return normalized response

## Recommended API

### `POST /transcribe`
Input:
- multipart audio upload or file path reference

Output:
```json
{
  "language": "en",
  "duration": 1850.4,
  "full_text": "...",
  "segments": [
    {
      "start": 0.0,
      "end": 9.2,
      "text": "Today we are learning about sorting algorithms"
    }
  ]
}
```

## Engineering notes
- normalize all time values to seconds
- always return segments in chronological order
- expose health endpoint
- add timeout controls
- log transcription duration

---

## 18. Quiz Generation Design

The quiz engine can be implemented in stages.

## MVP approach
- use summary chunks to create questions
- generate one or two questions per chunk
- attach source timestamp

## Question types
- multiple choice
- true/false
- short answer

## Required output structure
Each question should include:
- question text
- choices if applicable
- correct answer
- explanation
- `start_seconds`
- `end_seconds`

## Feedback behavior
If a user answers incorrectly:
- explain the correct concept
- provide a button like `Review this section`
- seek the video to the relevant timestamp

---

## 19. Security Requirements

### API Security
- authentication for user-specific actions
- authorization checks for video ownership
- rate limiting on process endpoint

### Input Validation
- validate YouTube URL structure
- limit file sizes if uploads are used later
- reject malformed inputs

### Infrastructure Security
- environment variables for secrets
- HTTPS in production
- secure database credentials
- container isolation

### Content Safety
- sanitize any HTML rendering
- avoid trusting third-party metadata blindly

---

## 20. Logging and Monitoring

Every service should have structured logs.

### What to log
- job creation
- stage changes
- external service failures
- transcription duration
- summary generation duration
- quiz generation duration
- user quiz submissions

### Monitoring targets
- error rate per endpoint
- average processing duration per job
- failed transcription count
- DB latency
- queue backlog

### Useful tools later
- Spring Boot Actuator
- Prometheus
- Grafana
- centralized logs

---

## 21. Dockerization Plan

Each service should be containerized.

## Containers
- frontend
- spring-backend
- whisper-service
- postgres
- redis
- nginx optional

## Docker Compose responsibilities
- local dev orchestration
- network wiring
- environment variable injection
- volume mapping for temp data if needed

---

## 22. Local Development Requirements

### Prerequisites
- Docker Desktop or Docker Engine
- Java 17+ or 21
- Node.js 20+
- Python 3.11+
- ffmpeg
- PostgreSQL if not using containerized DB locally

### Local environment variables
Backend:
- `SPRING_DATASOURCE_URL`
- `SPRING_DATASOURCE_USERNAME`
- `SPRING_DATASOURCE_PASSWORD`
- `REDIS_HOST`
- `WHISPER_SERVICE_URL`
- `JWT_SECRET`

Frontend:
- `VITE_API_BASE_URL`
- `VITE_YOUTUBE_EMBED_BASE`

Whisper service:
- `WHISPER_MODEL_SIZE`
- `TEMP_AUDIO_DIR`
- `MAX_AUDIO_DURATION`

---

## 23. Suggested File Structure

Below is a recommended monorepo-style structure.

```text
ai-assisted-learning-app/
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   │   ├── common/
│   │   │   │   ├── AppHeader.vue
│   │   │   │   ├── LoadingState.vue
│   │   │   │   └── ErrorState.vue
│   │   │   ├── video/
│   │   │   │   ├── VideoUrlForm.vue
│   │   │   │   ├── VideoPlayer.vue
│   │   │   │   └── ProcessingStatusCard.vue
│   │   │   ├── transcript/
│   │   │   │   ├── TranscriptList.vue
│   │   │   │   └── TranscriptSegmentItem.vue
│   │   │   ├── summary/
│   │   │   │   └── SummaryCard.vue
│   │   │   ├── quiz/
│   │   │   │   ├── QuizPanel.vue
│   │   │   │   └── QuestionCard.vue
│   │   │   └── progress/
│   │   │       └── ProgressStats.vue
│   │   ├── composables/
│   │   │   ├── useAuth.ts
│   │   │   ├── useVideos.ts
│   │   │   ├── useTranscript.ts
│   │   │   └── useQuiz.ts
│   │   ├── router/
│   │   │   └── index.ts
│   │   ├── stores/
│   │   │   ├── auth.ts
│   │   │   ├── video.ts
│   │   │   ├── transcript.ts
│   │   │   └── quiz.ts
│   │   ├── services/
│   │   │   ├── api.ts
│   │   │   ├── authService.ts
│   │   │   ├── videoService.ts
│   │   │   ├── transcriptService.ts
│   │   │   └── quizService.ts
│   │   ├── types/
│   │   │   ├── auth.ts
│   │   │   ├── video.ts
│   │   │   ├── transcript.ts
│   │   │   └── quiz.ts
│   │   ├── views/
│   │   │   ├── HomeView.vue
│   │   │   ├── ProcessVideoView.vue
│   │   │   ├── StudyView.vue
│   │   │   ├── QuizView.vue
│   │   │   └── DashboardView.vue
│   │   ├── App.vue
│   │   └── main.ts
│   ├── package.json
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   └── Dockerfile
│
├── backend/
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/com/example/ailearning/
│   │   │   │   ├── AiLearningApplication.java
│   │   │   │   ├── config/
│   │   │   │   ├── security/
│   │   │   │   ├── common/
│   │   │   │   ├── auth/
│   │   │   │   │   ├── controller/
│   │   │   │   │   ├── dto/
│   │   │   │   │   ├── service/
│   │   │   │   │   └── repository/
│   │   │   │   ├── video/
│   │   │   │   │   ├── controller/
│   │   │   │   │   ├── dto/
│   │   │   │   │   ├── entity/
│   │   │   │   │   ├── repository/
│   │   │   │   │   ├── service/
│   │   │   │   │   └── mapper/
│   │   │   │   ├── job/
│   │   │   │   ├── transcript/
│   │   │   │   ├── summary/
│   │   │   │   ├── quiz/
│   │   │   │   ├── progress/
│   │   │   │   ├── client/
│   │   │   │   │   └── WhisperClient.java
│   │   │   │   └── exception/
│   │   │   └── resources/
│   │   │       ├── application.yml
│   │   │       └── db/migration/
│   │   └── test/
│   ├── pom.xml
│   └── Dockerfile
│
├── whisper-service/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   └── routes.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── logging.py
│   │   ├── models/
│   │   │   └── schemas.py
│   │   ├── services/
│   │   │   ├── transcription_service.py
│   │   │   └── audio_service.py
│   │   └── utils/
│   │       └── time_utils.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── infra/
│   ├── nginx/
│   │   └── default.conf
│   ├── docker/
│   │   └── docker-compose.yml
│   └── scripts/
│       ├── setup-dev.sh
│       └── run-migrations.sh
│
├── docs/
│   ├── api-spec.md
│   ├── db-schema.md
│   ├── deployment.md
│   └── architect.md
│
├── .env.example
├── .gitignore
├── README.md
└── Architect.md
```

---

## 24. Step-by-Step Build Plan

## Phase 1: Project Setup
1. Create repo structure
2. Initialize Vue frontend with Vite
3. Initialize Spring Boot backend
4. Initialize FastAPI whisper service
5. Add Dockerfiles for all services
6. Add Docker Compose for local orchestration
7. Set up PostgreSQL and Redis

## Phase 2: Basic Backend Foundation
1. Add database schema and migrations
2. Add auth basics
3. Add video submission endpoint
4. Add job entity and job status tracking
5. Add health check endpoints

## Phase 3: Whisper Integration
1. Add audio extraction logic
2. Build `/transcribe` endpoint in Python
3. Add Spring client to call Whisper service
4. Persist transcript and transcript segments
5. Test the full transcription flow

## Phase 4: Summary Generation
1. Group transcript segments by time window
2. Generate summary blocks
3. Persist summary records
4. Expose summary endpoint
5. Render summaries in frontend

## Phase 5: Quiz System
1. Design quiz entity and schema
2. Create quiz generation logic
3. Create answer submission endpoint
4. Implement score calculation
5. Build quiz UI in Vue

## Phase 6: Interactive Learning UX
1. Add YouTube player
2. Add transcript click-to-seek
3. Add summary click-to-seek
4. Add quiz explanation jump-to-seek
5. Add progress tracking UI

## Phase 7: Production Hardening
1. Add auth protection
2. Add rate limiting
3. Improve error handling
4. Add logs and metrics
5. Add Nginx and deployment config

---

## 25. Development Order Recommendation

Build in this order to avoid overengineering too early.

### Must-build first
- URL submission
- job creation
- audio extraction
- Whisper transcription
- transcript display

### Then build
- summary generation
- summary display with timestamps

### Then build
- quiz generation
- quiz feedback
- quiz result storage

### Then build
- user accounts
- dashboards
- progress analytics

### Then optimize
- realtime streaming
- caching
- semantic search
- adaptive quiz difficulty

---

## 26. Testing Requirements

## Frontend Tests
- component rendering
- route navigation
- API integration mocks
- transcript click behavior

## Backend Tests
- controller tests
- service tests
- repository tests
- integration tests with test DB

## Whisper Service Tests
- endpoint tests
- schema validation tests
- long-audio failure handling

## End-to-End Tests
- submit video
- process transcript
- show summaries
- take quiz
- view results

---

## 27. Potential Risks and Solutions

### Risk: Long transcription time
Solution:
- async job processing
- visible status updates
- smaller Whisper model for dev

### Risk: Poor summary quality
Solution:
- better transcript chunking
- topic grouping later
- human-readable formatting rules

### Risk: Quiz irrelevance
Solution:
- generate from chunk summaries
- attach question to transcript evidence
- store explanations

### Risk: Complicated local setup
Solution:
- use Docker Compose
- provide `.env.example`
- provide setup scripts

### Risk: Tight coupling between Java and AI runtime
Solution:
- keep Whisper as standalone Python service

---

## 28. Recruiter-Strong Resume Framing

When this project is built, it can be described as:

> Built a full-stack AI learning platform using Vue, Spring Boot, PostgreSQL, Docker, and Whisper to convert educational YouTube videos into timestamped transcripts, topic-based summaries, and video-linked quizzes, enabling active learning and progress tracking through scalable asynchronous processing.

Strong ATS keywords from this project:
- Vue.js
- Java
- Spring Boot
- REST APIs
- PostgreSQL
- Redis
- Docker
- Microservices
- Whisper
- asynchronous job processing
- transcript processing
- quiz generation
- full-stack development
- scalable system design

---

## 29. MVP Definition

A good MVP is complete when the system can:
- accept a YouTube URL
- create a processing job
- transcribe the video with timestamps
- display transcript and summaries in frontend
- generate and submit a quiz
- save user results

Do not overbuild before the MVP works end-to-end.

---

## 30. Future Enhancements

After the MVP, possible upgrades include:
- multilingual transcription and quizzes
- semantic transcript search
- chapter auto-detection
- flashcards
- spaced repetition reminders
- note-taking linked to timestamps
- collaborative classrooms
- export to PDF or markdown study notes
- recommendation engine for related videos

---

## 31. Final Engineering Recommendations

1. Keep Whisper separate from Java.
2. Build the entire system around timestamped transcript segments because that is the most valuable data asset.
3. Make the first version async from the start.
4. Optimize for end-to-end completion before advanced AI features.
5. Keep the frontend deeply interactive because the learning UX is what differentiates the project.
6. Use clean modular architecture so the project reads like a real production system.

---

## 32. Immediate Next Tasks

If development starts now, the immediate next implementation tasks should be:

1. Create the monorepo structure
2. Scaffold Vue frontend
3. Scaffold Spring Boot backend
4. Scaffold FastAPI whisper service
5. Add Docker Compose with PostgreSQL and Redis
6. Implement `POST /api/videos/process`
7. Implement `/transcribe`
8. Persist transcript segments
9. Render transcript in Vue
10. Add summary generation

---

This document is intended to serve as the foundational architecture reference for designing and building the expanded AI-assisted educational video app.
