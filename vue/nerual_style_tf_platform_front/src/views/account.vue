<template>
      <div style="text-align: center; background-color: cornflowerblue; color: white; padding: 10px;">
    <h1 style="margin: 0; font-size: 24px;">Neural Style</h1>

  </div>
    <div class="account-container">
      <div id="account" class="account-box">
        <h1>Account</h1>
        <div class="user-info">
          <p><strong>Username:</strong> {{ userInfo.name }}</p>
          <p><strong>Email:</strong> {{ userInfo.email }}</p>
          <p><strong>UserID:</strong> {{ userInfo.id }}</p>
        </div>
        <el-input v-model="newUsername" placeholder="New Username" class="input-field"></el-input>
        <el-button type="primary" @click="updateUsername" class="action-button">Edit Username</el-button>
        <el-input v-model="newPassword" type="password" placeholder="New Password" class="input-field"></el-input>
        <el-button type="primary" @click="updatePassword" class="action-button">Edit Password</el-button>
        <el-button type="danger" @click="deleteAccount" class="action-button">Delete Account</el-button>
      </div>
    </div>
  </template>
  
  <script>
  import { getUserInfo, updateUsername, updatePassword, deleteAccount } from '../api';
  
  export default {
    name: 'Account',
    data() {
      return {
        userInfo: {
          name: '',
          email: '',
          id: ''
        },
        newUsername: '',
        newPassword: ''
      };
    },
    async created() {
      await this.fetchUserInfo();
    },
    methods: {
      async fetchUserInfo() {
        try {
          const response = await getUserInfo();
          this.userInfo = {
            name: response.name,
            email: response.email,
            id: response.id
          };
        } catch (error) {
          console.error('Fail to get user info:', error);
        }
      },
      async updateUsername() {
        try {
          await updateUsername({ name: this.newUsername });
          this.userInfo.name = this.newUsername;
          this.newUsername = '';
          location.reload();
        } catch (error) {
          console.error('Fail to change username:', error);
        }
      },
      async updatePassword() {
        try {
          await updatePassword({ password: this.newPassword });
          location.reload();
        } catch (error) {
          console.error('Fail to change password:', error);
        }
      },
      async deleteAccount() {
        try {
          await deleteAccount();
          location.reload();
        } catch (error) {
          console.error('Fail to delete account:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .account-container {
    background: url('/src/img/1.png') no-repeat center center;
    background-size: cover;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  
  .header {
    text-align: center;
    background-color: cornflowerblue;
    color: white;
    padding: 10px;
    width: 100%;
  }
  
  .account-box {
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 8px;
    padding: 30px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width: 350px;
    text-align: center;
  }
  
  .user-info {
    margin-bottom: 20px;
  }
  
  .input-field {
    margin-bottom: 15px;
    width: 100%;
  }
  
  .action-button {
    margin-bottom: 10px;
    width: 100%;
  }
  </style>