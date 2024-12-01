<template>
  <div class="flex flex-col overflow-hidden bg-white">
    <header class="ml-8 max-md:ml-2.5">
      <img
        loading="lazy"
        src="@/assets/ap-logo.png"
        alt="AI Assistant Logo"
        class="object-contain max-w-full aspect-[1.52] w-[156px]"
      />
    </header>
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
            <TabsTrigger value="tab2">Summary Generation</TabsTrigger>
            <TabsTrigger value="tab3">Quizzes</TabsTrigger>
          </TabsList>
          <TabsContent value="tab1" class="bg-violet-400">
<<<<<<< HEAD
            <!-- Content of Transcripts should go here -->
            <p>Content for Tab 1</p>
          </TabsContent>
          <TabsContent value="tab2">
            <!-- Content of Summaries should go here -->
            <p>Content for Tab 2</p>
          </TabsContent>

          <TabsContent value="tab3">
            <!-- Content of Quizzes should go here -->
            <p>Content for Tab 3</p>
=======
            <p v-if="loading">Loading content...</p> <!-- Display loading status -->
            <p v-else>{{ tab1Content }}</p> <!-- Dynamically render content -->
          </TabsContent>
          <TabsContent value="tab2" class="bg-violet-400">
            <p v-if="loading">Loading content...</p> <!-- Display loading status -->
            <p v-else>{{ tab2Content }}</p> <!-- Dynamically render content -->
          </TabsContent>

          <TabsContent value="tab3" class="bg-violet-400">
            <p v-if="loading">Loading content...</p> <!-- Display loading status -->
            <p v-else>{{ tab3Content }}</p> <!-- Dynamically render content -->
>>>>>>> new
          </TabsContent>
        </Tabs>
      </div>
    </main>
  </div>
</template>
<<<<<<< HEAD

=======
>>>>>>> new
<script>
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";

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
      tab1Content: '', // Content for Tab 1
      tab2Content: '', // Content for Tab 2
      tab3Content: '', // Content for Tab 3
      loadingTab1: true, // Loading status for Tab 1
      loadingTab2: true, // Loading status for Tab 2
      loadingTab3: true, // Loading status for Tab 3
    };
  },
  methods: {
    async fetchTab1Content() {
      this.loadingTab1 = true;
      try {
        //const response = await axios.get('/api/tab1-content');
        //this.tab1Content = response.data.content; // Response from the backend
        this.tab1Content = "1";
      } catch (error) {
        console.error('Error fetching Tab 1 content:', error);
        this.tab1Content = 'Failed to load content.';
      } finally {
        this.loadingTab1 = false;
      }
    },
    async fetchTab2Content() {
      this.loadingTab2 = true;
      try {
        //const response = await axios.get('/api/tab1-content');
        //this.tab1Content = response.data.content; // Response from the backend
        this.tab2Content = "2";
      } catch (error) {
        console.error('Error fetching Tab 2 content:', error);
        this.tab2Content = 'Failed to load content.';
      } finally {
        this.loadingTab2 = false;
      }
    },
    async fetchTab3Content() {
      try {
        //const response = await axios.get('/api/tab1-content');
        //this.tab1Content = response.data.content; // Response from the backend
        this.tab3Content = "3";
      } catch (error) {
        console.error('Error fetching Tab 3 content:', error);
        this.tab3Content = 'Failed to load content.';
      } finally {
        this.loadingTab3 = false;
      }
    },
    },
  mounted() {
    // Fetch content when the component is mounted
    this.fetchTab1Content();
    this.fetchTab2Content();
    this.fetchTab3Content();
  },
};
</script>
<style scoped>
main {
  height: 70vh; /* 70% of the viewport height */
}

.video-container {
  height: 100%;
  border-radius: 8px; /* Rounded corners */
  overflow: hidden; /* Ensure rounded corners work */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add shadow */
  background-color: #fff; /* Add background color */
}
iframe {
  width: 100%;
  height: 100%;
  border: none; /* Remove border */
}

.tabs-container {
  height: 100%;
  padding: 10px;
  border-radius: 8px;
  background-color: #ffffff; /* White background */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add shadow */
}
.tabs-trigger {
  display: inline-block;
  padding: 10px 15px;
  margin: 5px;
  background-color: #e0e7ff; /* Light blue background */
  color: #4f46e5; /* Dark blue text */
  border: 1px solid #dbeafe;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 500;
  text-align: center;
  transition: all 0.3s ease-in-out;
}
.tabs-trigger:hover {
  background-color: #c7d2fe; /* Deeper blue on hover */
}
.tabs-trigger[aria-selected="true"] {
  background-color: #4f46e5; /* Dark blue background when selected */
  color: #fff; /* White text */
}
.tabs-content {
  animation: fadeIn 0.3s ease-in-out;
  padding: 15px;
  border-radius: 8px;
  background-color: #f8fafc; /* Light gray background */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add shadow */
  color: #334155; /* Dark gray text color */
  font-size: 1rem;
  line-height: 1.5;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

</style>
