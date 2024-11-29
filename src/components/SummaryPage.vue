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
    <main>
      <div>Summary Section</div>
      <iframe
        v-if="videoUrl"
        :src="`https://www.youtube.com/embed/${videoUrl}`"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
        width="560"
        height="315"
      ></iframe>
    </main>
  </div>
</template>

<script>
export default {
  name: "SummaryPage",
  props: {
    videoUrl: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped>
h1 {
  font-size: 2em;
  text-align: center;
  margin-top: 20px;
}
</style>
