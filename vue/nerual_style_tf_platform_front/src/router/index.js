import { createRouter, createWebHistory } from 'vue-router';


const routes = [
  {
    path: '/',
    component:()=>import('../views/home.vue'),
  },
  {
    path: '/home',
    component:()=>import('../views/home.vue'),
  },
  {
    path: '/login',
    component:()=>import('../views/login.vue'),
  },
  {
    path: '/register',
    component:()=>import('../views/register.vue'),
  },
  {
    path: '/history',
    component:()=>import('../views/history.vue'),
  },
  {
    path: '/account',
    component:()=>import('../views/account.vue'),
  },
  {
    path: '/management',
    component:()=>import('../views/management.vue'),
  },
  {
    path: '/setting',
    component:()=>import('../views/setting.vue'),
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;