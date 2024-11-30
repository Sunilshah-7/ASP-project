<template>
  <div>
    <div class="max-md:max-w-full">
      <div class="flex gap-5 max-md:flex-col">
        <div class="flex flex-col w-[74%] max-md:ml-0 max-md:w-full">
          <div
            class="z-10 flex flex-col self-stretch my-auto mr-0 font-light text-black max-md:mt-10 max-md:max-w-full"
          >
            <h1 class="text-5xl max-md:max-w-full max-md:text-4xl">
              <span class="font-bold text-indigo-600">AI Assistant</span>
              for your next youtube video
            </h1>
            <p class="self-start mt-4 text-3xl max-md:max-w-full">
              Your personal tool to help you summarize, question and educate in
              an
              <span class="font-bold text-indigo-600">interactive</span>
              manner
            </p>
          </div>
        </div>
        <div class="flex flex-col ml-5 w-[26%] max-md:ml-0 max-md:w-full">
          <img
            loading="lazy"
            src="@/assets/sideimage-for-project.png"
            alt="AI Assistant Illustration"
            class="object-contain grow w-full aspect-[1.03]"
          />
        </div>
      </div>
    </div>
    <form
      @submit.prevent="handleSubmit"
      class="flex items-center gap-5 mt-2.5 -mb-6 w-full text-xl max-w-[1920px] max-md:mb-2.5 max-md:max-w-full"
    >
      <label for="youtubeLink" class="sr-only"
        >Paste your youtube video link here</label
      >
      <input
        id="youtubeLink"
        v-model="youtubeUrl"
        type="text"
        placeholder="Paste your youtube video link here........."
        class="w-4/5 px-2.5 py-5 font-light text-black bg-white rounded-xl border-solid border-[3px] border-stone-200 min-h-[70px] shadow-[0px_4px_4px_rgba(0,0,0,0.25)] max-md:max-w-full"
      />
      <button
        type="submit"
        class="w-1/5 flex justify-center items-center text-white whitespace-nowrap bg-indigo-600 rounded-xl min-h-[70px]"
      >
        <span class="self-stretch gap-1 my-auto">Interact</span>
      </button>
    </form>
  </div>
</template>

<script>
export default {
  name: "HeroSection",
  data() {
    return {
      youtubeUrl: "",
    };
  },
  methods: {
    async handleSubmit() {
      const videoId = this.youtubeUrl.split("v=")[1]?.split("&")[0];
      if (videoId) {
        //const response = await axios.post("http://localhost:3000/api/process-video", { videoId });
        this.$router.push({ path: "/summary", query: { v: videoId } });
      } else {
        alert("Please enter a valid YouTube URL.");
      }
    },
  },
};
</script>

<style lang=""></style>
