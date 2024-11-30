import { createWebHistory, createRouter } from "vue-router";
import SummaryPage from "@/components/SummaryPage.vue";
import AiAssistantPage from "@/components/AiAssistantPage.vue";

const routes = [
  {
    path: "/",
    name: "AiAssistantPage",
    component: AiAssistantPage,
  },
  {
    path: "/summary",
    name: "SummaryPage",
    component: SummaryPage,
    props: (route) => ({ videoUrl: route.query.v }),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
