<template>
  <div class="w-full">
    <div class="flex gap-5 max-md:flex-col">
      <div class="flex flex-col w-[43%] max-md:ml-0 max-md:w-full">
        <img
          loading="lazy"
          src="@/assets/lightbulb.png"
          alt="Features illustration"
          class="object-contain mt-3 w-full aspect-[1.14] max-md:mt-10"
        />
      </div>
      <div class="flex flex-col ml-5 w-[57%] max-md:ml-0 max-md:w-full">
        <div class="flex flex-col grow max-md:mt-10">
          <h2
            class="self-start ml-2.5 text-5xl font-bold text-indigo-600 max-md:text-4xl"
          >
            Features:
          </h2>
          <ul
            class="text-4xl font-light text-black border border-black border-solid mt-14 max-md:mt-10"
          >
            <li>Chat with your video</li>
            <li>Generate insights</li>
            <li>Quizzes to remember</li>
            <li>Detect your solution</li>
            <li>Get your code</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "FeaturesSection",
  
};
</script>
<style lang=""></style>
