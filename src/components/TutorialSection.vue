<template>
  <div class="flex gap-5 max-md:flex-col">
    <div class="flex flex-col w-[65%] max-md:ml-0 max-md:w-full">
      <div class="flex flex-col max-md:mt-10 max-md:max-w-full">
        <h2
          class="self-start text-5xl font-bold text-indigo-600 max-md:text-4xl"
        >
          How it works?
        </h2>

        <ol
          class="text-4xl font-light text-black border border-black border-solid mt-14 max-md:mt-10 max-md:max-w-full"
        >
          <li>Paste your tutorial in the text box.</li>

          <li>Press the Interact button.</li>
          <li>
            Watch your favorite video with it and
            <span class="text-indigo-600">mainly </span>ask questions to your
            video.
          </li>
        </ol>
      </div>
    </div>
    <div class="flex flex-col ml-5 w-[35%] max-md:ml-0 max-md:w-full">
      <img
        loading="lazy"
        src="@/assets/questionmark.png"
        alt="How it works illustration"
        class="object-contain grow w-full aspect-[0.96] max-md:mt-10"
      />
    </div>
  </div>
</template>
<script>
export default {
  name: "TutorialSection",
};
</script>
<style lang=""></style>
