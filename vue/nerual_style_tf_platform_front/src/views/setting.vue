<template>
  <div style="text-align: center; background-color: cornflowerblue; color: white; padding: 10px;">
    <h1 style="margin: 0; font-size: 24px;">Neural Style</h1>
  </div>
  <button @click="navigateToHome" style="background-color:darkgray; color:white; padding: 5px;">Back</button>
  <div id="setting" style="display: flex; justify-content: center; align-items: center; height: 100vh; flex-direction: column;">
    <h1>Setting Page</h1>
    <!-- Add more settings options here -->
  </div>
</template>

<script>
export default {
  name: 'Setting',
  methods: {
    navigateToHome() {
      this.$router.push('/home');
    }
  }
};
</script>