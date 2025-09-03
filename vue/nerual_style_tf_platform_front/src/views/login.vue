<template>
    <div style="text-align: center; background-color: cornflowerblue; color: white; padding: 10px;">
    <h1 style="margin: 0; font-size: 24px;">Neural Style</h1>

  </div>
  <div class="login-container">
    <el-container style="height: 100vh; overflow: hidden;">
      <el-main style="display: flex; justify-content: flex-end; align-items: center; position: relative;">
        <div class="login-box">
          <el-form @submit.prevent="handleLogin" style="width: 300px; margin-right: 50px;">
            <h2>Login</h2>
            <el-form-item>
              <el-input v-model="username" placeholder="Username"></el-input>
            </el-form-item>
            <el-form-item>
              <el-input type="password" v-model="password" placeholder="Password"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="handleLogin">Login</el-button>
              <el-button @click="goToRegister">Register</el-button>
            </el-form-item>
          </el-form>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import axios from 'axios';
import { ElForm, ElInput, ElButton } from 'element-plus';

export default {
  name: 'Login',
  components: {
    ElForm,
    ElInput,
    ElButton
  },
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    handleLogin() {
      axios.post('http://localhost:5000/login', {
        username: this.username,
        password: this.password,
      })
      .then(response => {
        if (response.data.message === 'Login successful') {
          alert('Login successful');
          this.$router.push('/home');
        } else {
          alert('wrong username or password');
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
    },
    goToRegister() {
      this.$router.push('/register');
    },
  },
};
</script>

<style scoped>
.login-container {
  background: url('/src/img/1.png') no-repeat center center;
  background-size: cover;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.header {
  text-align: center;
  background-color: cornflowerblue;
  color: white;
  padding: 10px;
  width: 100%;
}

.login-box {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.8);
}
</style>