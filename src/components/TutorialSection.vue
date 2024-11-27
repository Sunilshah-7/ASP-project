<template>
  <div class="flex gap-5 max-md:flex-col">
    <div class="flex flex-col w-[65%] max-md:ml-0 max-md:w-full">
      <div class="flex flex-col max-md:mt-10 max-md:max-w-full">
        <h2
          class="self-start text-5xl font-bold text-indigo-600 max-md:text-4xl"
        >
          How it works?
        </h2>

        <ul
          class="grid grid-cols-2 gap-4 text-4xl font-light mt-14 max-md:mt-10"
        >
          <li>
            <Card
              class="p-5 transition duration-300 bg-indigo-100 rounded-lg shadow-lg hover:bg-indigo-200 hover:shadow-xl"
            >
              <CardHeader>
                <CardTitle class="font-semibold text-indigo-700"
                  >Paste your tutorial in the text box.</CardTitle
                >
              </CardHeader>
            </Card>
          </li>
          <li>
            <Card
              class="p-5 transition duration-300 bg-green-100 rounded-lg shadow-lg hover:bg-green-200 hover:shadow-xl"
            >
              <CardHeader>
                <CardTitle class="font-semibold text-green-700"
                  >Press the Interact button.</CardTitle
                >
              </CardHeader>
            </Card>
          </li>
          <li>
            <Card
              class="p-5 transition duration-300 bg-yellow-100 rounded-lg shadow-lg hover:bg-yellow-200 hover:shadow-xl"
            >
              <CardHeader>
                <CardTitle class="font-semibold text-yellow-700"
                  >Watch your favorite video with it and
                  <span class="text-indigo-600">mainly </span>ask questions to
                  your video.</CardTitle
                >
              </CardHeader>
            </Card>
          </li>
        </ul>
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
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import "@/assets/index.css";
export default {
  name: "TutorialSection",
  components: {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
  },
};
</script>
<style lang=""></style>
