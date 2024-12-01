<template>
  <div class="flex flex-col overflow-hidden">
    <header class="ml-8 max-md:ml-2.5">
      <img
        loading="lazy"
        src="@/assets/ap-logo.png"
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
                <div v-for="(topic, index) in summary" :key="index">
                  <h3>{{ topic.main_topic }}</h3>
                  <p>
                    <strong>Time Range:</strong> {{ topic.time_start }} -
                    {{ topic.time_end }}
                  </p>
                  <ul>
                    <li
                      v-for="(subtopic, subIndex) in topic.subtopics"
                      :key="subIndex"
                    >
                      {{ subtopic }}
                    </li>
                  </ul>
                </div>
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
                    <button @click="submitAnswer('True')">True</button>
                    <button @click="submitAnswer('False')">False</button>
                  </div>
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
                  <button @click="restartQuiz">Restart Quiz</button>
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
    };
  },
  methods: {
    async fetchTranscript() {
      this.loadingTab1 = true;
      try {
        const response = await getTranscript();
        this.transcripts = response;
        console.log("Transcript data:", this.transcripts);
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
        const response = await fetch("/summary.json"); // Local file fetch
        this.summary = await response.json();
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
        const response = await fetch("/quiz.json"); // Local file fetch
        this.quizzes = await response.json();
      } catch (error) {
        console.error("Error fetching quizzes:", error);
        toast.error("Failed to load quizzes.");
      } finally {
        this.loadingTab3 = false;
      }
    },
    submitAnswer(answer) {
      if (answer === this.quizzes[this.currentQuizIndex].correct_answer) {
        this.correctAnswers++;
        this.feedback = "Correct!";
      } else {
        this.feedback =
          "Wrong! The correct answer is " +
          this.quizzes[this.currentQuizIndex].correct_answer +
          ".";
      }
      setTimeout(() => {
        this.feedback = "";
        this.currentQuizIndex++;
      }, 1000);
    },
    restartQuiz() {
      this.currentQuizIndex = 0;
      this.correctAnswers = 0;
      this.feedback = "";
    },
  },
  mounted() {
    // Restore local fetch methods
    this.fetchTranscript();
    this.fetchSummary();
    this.fetchQuizzes();
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
  height: 500px;
  overflow-y: auto;
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
.options button {
  display: block;
  margin: 10px 0;
  padding: 10px;
  font-size: 16px;
  cursor: pointer;
}
.feedback {
  margin-top: 10px;
  font-size: 16px;
  color: green;
}
</style>
