<template>
    <div id="prepare">
      <router-view></router-view>
      <button @click="goToLogin" class="center-button">进入登录界面</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Prepare',
    methods: {
      goToLogin() {
        this.$router.push('/login'); // 导航到登录界面
      },
      checkLoginStatus() {
        const isLoggedIn = localStorage.getItem('token'); // 检查 token 是否存在
        if (isLoggedIn) {
          this.$router.push('/home'); // 如果已登录，导航到主页
        }
      }
    },
    mounted() {
      this.checkLoginStatus(); // 检查登录状态
    }
  };
  </script>
  
  <style>
  #app {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  
  .center-button {
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
  }
  </style>