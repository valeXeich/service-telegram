import { createRouter, createWebHistory } from "vue-router";
import Main from "@/components/Main.vue";
import Login from "@/components/Login.vue";
import Cabinet from '@/components/Cabinet.vue';
import AccountDetail from '@/components/AccountDetail.vue';
import CabinetSettings from '@/components/CabinetSettings.vue'


const routes = [
  {
    path: "/",
    component: Main,
  },
  {
    path: "/login",
    component: Login,
  },
  {
    path: "/cabinet",
    component: Cabinet,
  },
  {
    path: "/cabinet/detail/:id",
    component: AccountDetail,
  },
  {
    path: "/cabinet/settings",
    component: CabinetSettings,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
