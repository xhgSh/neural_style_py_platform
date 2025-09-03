<template>
    <div style="text-align: center; background-color: cornflowerblue; color: white; padding: 10px;">
    <h1 style="margin: 0; font-size: 24px;">Neural Style</h1>

  </div>
  <el-container style="height: 100vh;">
    <!-- Header -->


    <el-container>
      <!-- Sidebar -->
      <el-aside width="200px" style="background-color: #f2f2f2;">
        <el-menu>
          <el-menu-item index="2">
            <button class="blueButtom" @click="navigateTo('/account')">Account</button>
          </el-menu-item>
          <el-menu-item index="1">
            <button class="blueButtom" @click="navigateTo('/history')">History</button>
          </el-menu-item>

          <el-menu-item index="3">
            <button class="blueButtom" @click="goToManagement">Management</button>
          </el-menu-item>
          <!-- <el-menu-item index="4">
            <button class="blueButtom" @click="navigateTo('/setting')">Setting</button>
          </el-menu-item> -->
        </el-menu>
      </el-aside>

      <!-- Main Content -->
      <el-main>
        <div class="navbar-right" style="text-align: right; margin-bottom: 20px;">
          <template v-if="userName">
            <span>user: {{ userName }}</span>
            <el-button type="primary" @click="signOut">Sign Out</el-button>
          </template>
          <template v-else>
            <button class="blueButtom" @click="navigateTo('/login')">Login</button>
            <button class="blueButtom" @click="navigateTo('/register')">Register</button>
          </template>
        </div>

        <div class="content">
          <h2>Upload Content and Style Images</h2>
          <label for="content-image">Content Image:  </label>
          
          <input id="content-image" type="file" @change="onContentFileChange" placeholder="Content Image" />
          <label for="style-image">Style Image:  </label>
          <input id="style-image" type="file" @change="onStyleFileChange" placeholder="Style Image" />
          <el-button @click="uploadImages" :disabled="isLoading">Transfer</el-button>
          <p v-if="isLoading">Loading...</p>
          <div v-if="generatedImageUrl && !isLoading">
            <h3>Generated Image</h3>
            <img :src="`http://localhost:5000${generatedImageUrl}`" alt="Generated Image" style="max-width: 100%; height: auto;" />
            <a :href="`http://localhost:5000${generatedImageUrl}`" download>
              <el-button>Download Image</el-button>
            </a>
          </div>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
  data() {
    return {
      contentFile: null,
      styleFile: null,
      userName: null,
      isadmin: false,
      generatedImageUrl: null,
      isLoading: false,
    };
  },
  methods: {
    async getUserInfo() {
      try {
        const response = await axios.get('http://localhost:5000/api/getUserInfo');
        this.userName = response.data.name;
        this.isadmin = response.data.isadmin;
      } catch (error) {
        console.error('Error getting user info:', error);
      }
    },
    onContentFileChange(event) {
      this.contentFile = event.target.files[0];
    },
    onStyleFileChange(event) {
      this.styleFile = event.target.files[0];
    },
    async uploadImages() {
      if (!this.contentFile || !this.styleFile) {
        alert('Please select both content and style images to upload.');
        return;
      }

      this.isLoading = true;

      const formData = new FormData();
      formData.append('content', this.contentFile);
      formData.append('style', this.styleFile);

      try {
        const response = await axios.post('http://localhost:5000/transfer', formData);
        this.generatedImageUrl = response.data.url;
        alert('Images transferred successfully. Generated image URL: ' + response.data.url);
      } catch (error) {
        console.error('Error uploading images:', error);
        alert('Failed to upload images.');
      } finally {
        this.isLoading = false;
      }
    },
    async signOut() {
      await axios.post('http://localhost:5000/logout');
      this.userName = null;
      this.isadmin = false;
      this.$router.push('/login');
    },
    async goToManagement() {
      if (!this.isadmin) {
        alert('you are not administrator');
      } else {
        this.$router.push('/management');
      }
    },
    navigateTo(path) {
      this.$router.push(path);
    }
  },
  mounted() {
    this.getUserInfo();
  },
};
</script>

<style scoped>
.content {
  margin-top: 20px;
  text-align: center;
}
</style>