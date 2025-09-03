<template>
  <div style="text-align: center; background-color: cornflowerblue; color: white; padding: 10px;">
    <h1 style="margin: 0; font-size: 24px;">Neural Style</h1>
  </div>
  <div class="register-container">

    <el-container style="height: 100vh; overflow: hidden;">
      <el-main style="display: flex; justify-content: flex-end; align-items: center; position: relative;">
        <div class="register-box">
          <el-form @submit.prevent="handleRegister" style="width: 300px; margin-right: 50px;">
            <h2>Register</h2>
            <el-form-item>
              <el-input v-model="name" placeholder="Name"></el-input>
            </el-form-item>
            <el-form-item>
              <el-input v-model="email" placeholder="Email"></el-input>
            </el-form-item>
            <el-form-item>
              <el-input type="password" v-model="password" placeholder="Password"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="handleRegister">Register</el-button>
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
  name: 'Register',
  components: {
    ElForm,
    ElInput,
    ElButton
  },
  data() {
    return {
      name: '',
      email: '',
      password: '',
    };
  },
  methods: {
    handleRegister() {
      axios.post('http://localhost:5000/register', {
        name: this.name,
        password: this.password,
        email: this.email,
      })
      .then(response => {
        if (response.data.message === 'User registered successfully') {
          alert('Registration successful');
          this.$router.push('/login');
        } else {
          alert('Registration failed');
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
    },
  },
};
</script>

<style scoped>
.register-container {
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

.register-box {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.8);
}
</style>