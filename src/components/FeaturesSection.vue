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
            class="grid grid-cols-2 gap-4 text-4xl font-light mt-14 max-md:mt-10"
          >
            <li>
              <Card
                class="p-5 transition duration-300 bg-indigo-100 rounded-lg shadow-lg hover:bg-indigo-200 hover:shadow-xl"
              >
                <CardHeader>
                  <CardTitle class="font-semibold text-indigo-700"
                    >Chat with your video</CardTitle
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
                    >Generate insights</CardTitle
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
                    >Quizzes to remember</CardTitle
                  >
                </CardHeader>
              </Card>
            </li>
            <li>
              <Card
                class="p-5 transition duration-300 bg-red-100 rounded-lg shadow-lg hover:bg-red-200 hover:shadow-xl"
              >
                <CardHeader>
                  <CardTitle class="font-semibold text-red-700"
                    >Get your code</CardTitle
                  >
                </CardHeader>
              </Card>
            </li>
          </ul>
        </div>
      </div>
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
  name: "FeaturesSection",
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
