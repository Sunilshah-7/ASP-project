<template>
  <div class="flex overflow-hidden flex-col bg-white">
    <header class="ml-8 max-md:ml-2.5">
      <img
        loading="lazy"
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/b5bfb4d5c63e39bdd1aadf104ed05176c161ba7ad829c7725318d8c244351c2d?placeholderIfAbsent=true&apiKey=26babde2ec0e40baafbcc47b204b6c36"
        alt="AI Assistant Logo"
        class="object-contain max-w-full aspect-[1.52] w-[156px]"
      />
    </header>
    <main>
      <section
        class="flex flex-col pt-14 pb-32 pl-20 w-full bg-violet-400 max-md:pb-24 max-md:pl-5 max-md:max-w-full"
      >
        <div class="max-md:max-w-full">
          <div class="flex gap-5 max-md:flex-col">
            <div class="flex flex-col w-[74%] max-md:ml-0 max-md:w-full">
              <div
                class="flex z-10 flex-col self-stretch my-auto mr-0 font-light text-black max-md:mt-10 max-md:max-w-full"
              >
                <h1 class="text-5xl max-md:max-w-full max-md:text-4xl">
                  <span class="font-bold text-indigo-600">AI Assistant</span>
                  for your next youtube video
                </h1>
                <p class="self-start mt-4 ml-11 text-3xl max-md:max-w-full">
                  Your personal tool to help you summarize, question and educate
                  in an
                  <span class="font-bold text-indigo-600">interactive</span>
                  manner
                </p>
              </div>
            </div>
            <div class="flex flex-col ml-5 w-[26%] max-md:ml-0 max-md:w-full">
              <img
                loading="lazy"
                src="https://cdn.builder.io/api/v1/image/assets/TEMP/da18de862f512091a56c433226c1f3eda46d07929aa842767337d62a1ab19fcb?placeholderIfAbsent=true&apiKey=26babde2ec0e40baafbcc47b204b6c36"
                alt="AI Assistant Illustration"
                class="object-contain grow w-full aspect-[1.03]"
              />
            </div>
          </div>
        </div>
        <form
          class="flex flex-wrap gap-5 mt-2.5 -mb-6 w-full text-xl max-w-[1063px] max-md:mb-2.5 max-md:max-w-full"
        >
          <label for="youtubeLink" class="sr-only"
            >Paste your youtube video link here</label
          >
          <input
            id="youtubeLink"
            type="text"
            placeholder="Paste your youtube video link here........."
            class="flex-auto gap-2.5 self-stretch px-2.5 py-5 font-light text-black bg-white rounded-xl border-solid border-[3px] border-stone-200 min-h-[70px] shadow-[0px_4px_4px_rgba(0,0,0,0.25)] w-[666px] max-md:max-w-full"
          />
          <button
            type="submit"
            class="flex justify-between items-center px-4 py-5 text-white whitespace-nowrap bg-indigo-600 rounded-xl min-h-[70px]"
          >
            <span class="gap-1 self-stretch my-auto">Interact</span>
          </button>
        </form>
      </section>
      <section
        class="flex flex-col self-center mt-24 w-full max-w-[1071px] max-md:mt-10 max-md:max-w-full"
      >
        <div class="max-md:max-w-full">
          <div class="flex gap-5 max-md:flex-col">
            <div class="flex flex-col w-[65%] max-md:ml-0 max-md:w-full">
              <div class="flex flex-col max-md:mt-10 max-md:max-w-full">
                <h2
                  class="self-start text-5xl font-bold text-indigo-600 max-md:text-4xl"
                >
                  How it works?
                </h2>
                <ol
                  class="mt-14 text-4xl font-light text-black border border-black border-solid max-md:mt-10 max-md:max-w-full"
                >
                  <li>Paste your tutorial in the text box.</li>
                  <li>Press the Interact button.</li>
                  <li>
                    Watch your favorite video with it and
                    <span class="text-indigo-600">mainly </span>ask questions to
                    your video.
                  </li>
                </ol>
              </div>
            </div>
            <div class="flex flex-col ml-5 w-[35%] max-md:ml-0 max-md:w-full">
              <img
                loading="lazy"
                src="https://cdn.builder.io/api/v1/image/assets/TEMP/3b1b1af3d0ca0b919f313aca2a849ce8800b58814fda3d13046f48b4011f9ed1?placeholderIfAbsent=true&apiKey=26babde2ec0e40baafbcc47b204b6c36"
                alt="How it works illustration"
                class="object-contain grow w-full aspect-[0.96] max-md:mt-10"
              />
            </div>
          </div>
        </div>
        <div class="mt-28 ml-4 max-w-full w-[860px] max-md:mt-10">
          <div class="flex gap-5 max-md:flex-col">
            <div class="flex flex-col w-[43%] max-md:ml-0 max-md:w-full">
              <img
                loading="lazy"
                src="https://cdn.builder.io/api/v1/image/assets/TEMP/3bb66596573a0916b6b3a1c39e7e9a75f2b959beb78dd85d1acfc0306872cac9?placeholderIfAbsent=true&apiKey=26babde2ec0e40baafbcc47b204b6c36"
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
                  class="mt-14 text-4xl font-light text-black border border-black border-solid max-md:mt-10"
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
      </section>
    </main>
    <footer
      class="flex flex-col justify-center items-center px-16 py-8 mt-16 w-full bg-violet-400 max-md:px-5 max-md:mt-10 max-md:max-w-full"
    >
      <div class="w-full max-w-[1056px] max-md:max-w-full">
        <h2
          class="self-start text-5xl font-bold text-black max-md:max-w-full max-md:text-4xl"
        >
          Our Innovative Team
        </h2>
        <div class="flex gap-5 max-md:flex-col">
          <div class="flex flex-col w-[23%] max-md:ml-0 max-md:w-full">
            <div
              class="flex flex-col mt-32 text-xl font-bold tracking-tight text-center text-black max-md:mt-10"
            >
              <img
                loading="lazy"
                src="https://cdn.builder.io/api/v1/image/assets/TEMP/8c6917484ccb19dc08cf8ebfc545fdf79d3eae1a53f908807bb6d4bb49ea501f?placeholderIfAbsent=true&apiKey=26babde2ec0e40baafbcc47b204b6c36"
                alt="Keith Zhang"
                class="object-contain w-full rounded-full aspect-[1.07]"
              />
              <p class="self-center mt-7">Keith Zhang</p>
              <img
                loading="lazy"
                src="https://cdn.builder.io/api/v1/image/assets/TEMP/8c6917484ccb19dc08cf8ebfc545fdf79d3eae1a53f908807bb6d4bb49ea501f?placeholderIfAbsent=true&apiKey=26babde2ec0e40baafbcc47b204b6c36"
                alt="Chris Gomez"
                class="object-contain mt-10 w-full rounded-full aspect-[1.07]"
              />
              <p class="self-center mt-4">Chris Gomez</p>
            </div>
          </div>
          <div class="flex flex-col ml-5 w-[77%] max-md:ml-0 max-md:w-full">
            <div class="flex flex-col grow max-md:mt-5 max-md:max-w-full">
              <div
                class="flex flex-col self-end mt-20 max-w-full w-[641px] max-md:mt-10"
              >
                <div class="max-md:max-w-full">
                  <div class="flex gap-5 max-md:flex-col">
                    <div class="flex flex-col w-6/12 max-md:ml-0 max-md:w-full">
                      <div
                        class="flex flex-col grow text-xl font-bold tracking-tight text-center text-black max-md:mt-10"
                      >
                        <img
                          loading="lazy"
                          src="https://cdn.builder.io/api/v1/image/assets/TEMP/9187519db88f28d12a6dc1d678c3eb73a04036e286842ffe8165b521d71a8f8d?placeholderIfAbsent=true&apiKey=26babde2ec0e40baafbcc47b204b6c36"
                          alt="Yuming Shi"
                          class="object-contain w-full rounded-full aspect-[1.07]"
                        />
                        <p class="self-center mt-7">Yuming Shi</p>
                      </div>
                    </div>
                    <div
                      class="flex flex-col ml-5 w-6/12 max-md:ml-0 max-md:w-full"
                    >
                      <div
                        class="flex flex-col text-xl font-bold tracking-tight text-center text-black max-md:mt-10"
                      >
                        <img
                          loading="lazy"
                          src="https://cdn.builder.io/api/v1/image/assets/TEMP/3c7dc5e922fbc1db908c8d5dbe81c062ff6d388535873aaa16467adc8c233787?placeholderIfAbsent=true&apiKey=26babde2ec0e40baafbcc47b204b6c36"
                          alt="Sunil Shah"
                          class="object-contain w-full rounded-full aspect-[1.07]"
                        />
                        <p class="self-center mt-7 ml-6">Sunil Shah</p>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="mt-10 max-md:max-w-full">
                  <div class="flex gap-5 max-md:flex-col">
                    <div class="flex flex-col w-6/12 max-md:ml-0 max-md:w-full">
                      <div
                        class="flex flex-col text-xl font-bold tracking-tight text-center text-black max-md:mt-10"
                      >
                        <img
                          loading="lazy"
                          src="https://cdn.builder.io/api/v1/image/assets/TEMP/9187519db88f28d12a6dc1d678c3eb73a04036e286842ffe8165b521d71a8f8d?placeholderIfAbsent=true&apiKey=26babde2ec0e40baafbcc47b204b6c36"
                          alt="Kishan KC"
                          class="object-contain w-full rounded-full aspect-[1.07]"
                        />
                        <p class="self-center mt-6">Kishan KC</p>
                      </div>
                    </div>
                    <div
                      class="flex flex-col ml-5 w-6/12 max-md:ml-0 max-md:w-full"
                    >
                      <div
                        class="flex flex-col grow text-xl font-bold tracking-tight text-center text-black max-md:mt-10"
                      >
                        <img
                          loading="lazy"
                          src="https://cdn.builder.io/api/v1/image/assets/TEMP/3c7dc5e922fbc1db908c8d5dbe81c062ff6d388535873aaa16467adc8c233787?placeholderIfAbsent=true&apiKey=26babde2ec0e40baafbcc47b204b6c36"
                          alt="Haoyu Guo"
                          class="object-contain w-full rounded-full aspect-[1.07]"
                        />
                        <p class="self-end mt-7 mr-11 max-md:mr-2.5">
                          Haoyu Guo
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "AIAssistantPage",
  // Add any necessary component logic here
});
</script>
