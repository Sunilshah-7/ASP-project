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
          </TabsContent>
        </Tabs>
      </div>
    </main>
  </div>
</template>

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
};
</script>

<style scoped>
main {
  height: 70vh; /* 70% of the viewport height */
}

.video-container {
  height: 100%;
}

iframe {
  width: 100%;
  height: 100%;
}

.tabs-container {
  height: 100%;
  margin-left: 16px; /* Add left margin to make tabs distinct */
}

.tabs-trigger {
  width: 100%; /* Make each tab trigger cover the full width */
  display: block; /* Ensure the tab trigger is a block element */
  text-align: center; /* Center the text */
  padding: 10px 0; /* Add some padding for better appearance */
  box-sizing: border-box; /* Include padding in the element's total width and height */
  font-size: 1.25rem; /* Increase font size */
  margin: 0 auto; /* Center horizontally */
}
</style>
