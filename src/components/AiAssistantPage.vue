<template>
  <div class="flex flex-col overflow-hidden bg-white">
    <header class="ml-8 max-md:ml-2.5">
      <img
        loading="lazy"
        src="@/assets/home-logo.png"
        alt="AI Assistant Logo"
        class="object-contain max-w-full aspect-[1.52] w-[156px]"
      />
    </header>
    <main>
      <section
        class="flex flex-col w-full px-20 py-14 bg-violet-400 max-md:py-10 max-md:px-5 max-md:max-w-full"
      >
        <HeroSection />
      </section>
      <section
        class="flex flex-col w-full px-20 py-14 max-md:py-10 max-md:max-w-full"
      >
        <div class="max-md:max-w-full">
          <TutorialSection />
          <FeaturesSection />
        </div>
        <!-- <SummaryPage videoUrl="https://www.youtube.com/watch?v=Onf7AKGHBzg" /> -->
      </section>
    </main>
    <footer
      class="flex flex-col items-center justify-center w-full px-16 py-8 mt-16 bg-violet-400 max-md:px-5 max-md:mt-10 max-md:max-w-full"
    >
      <TeamSection />
    </footer>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import HeroSection from "./HeroSection.vue";
import TeamSection from "./TeamSection.vue";
import FeaturesSection from "./FeaturesSection.vue";
import TutorialSection from "./TutorialSection.vue";
import SummaryPage from "./SummaryPage.vue";
export default defineComponent({
  name: "AIAssistantPage",
  components: {
    HeroSection,
    TeamSection,
    FeaturesSection,
    TutorialSection,
    SummaryPage,
  },
});
</script>
