<template>
  <div style="text-align: center; background-color: cornflowerblue; color: white; padding: 10px;">
    <h1 style="margin: 0; font-size: 24px;">Neural Style</h1>
  </div>
  <button @click="navigateToHome" style="background-color:darkgray; color:white; padding: 5px;">Back</button>
  <div id="management" style="display: flex; justify-content: center; align-items: center; height: 100vh; flex-direction: column;">

    <h1>Management Page</h1>
    <div v-if="errorMessage">{{ errorMessage }}</div>
    <table v-if="users.length > 0">
      <thead>
        <tr>
          <th>User id</th>
          <th>Name</th>
          <th>Email</th>
          <th>Delete</th>
          <th>Promote</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.id">
          <td>{{ user.id }}</td>
          <td>{{ user.name }}</td>
          <td>{{ user.email }}</td>
          <td>
            <button @click="deleteUser(user.id)">Delete</button>
          </td>
          <td>
            <button v-if="!user.is_admin" @click="promoteToAdmin(user.id)">Promote to Admin</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { getUsers, deleteUser as deleteUserApi, promoteToAdmin as promoteToAdminApi } from '../api';

export default {
  name: 'Management',
  data() {
    return {
      users: [],
      errorMessage: ''
    };
  },
  methods: {
    async fetchUsers() {
      try {
        const response = await getUsers();
        this.users = response;
      } catch (error) {
        if (error.response && error.response.status === 403) {
          this.errorMessage = 'no permission';
        } else {
          console.error('Error fetching users:', error);
          this.errorMessage = 'fail to get user info';
        }
      }
    },
    async deleteUser(userId) {
      try {
        await deleteUserApi(userId);
        this.fetchUsers();
      } catch (error) {
        console.error('Error deleting user:', error);
      }
    },
    async promoteToAdmin(userId) {
      try {
        await promoteToAdminApi(userId);
        this.fetchUsers();
      } catch (error) {
        console.error('Error promoting user to admin:', error);
      }
    },
    navigateToHome() {
      this.$router.push('/home');
    }
  },
  mounted() {
    this.fetchUsers();
  }
};
</script>

<style scoped>
table {
  width: 80%;
  margin: 20px auto;
  border-collapse: separate;
  border-spacing: 0;
  box-shadow: 0 2px 3px rgba(0,0,0,0.1);
  border-radius: 5px;
  overflow: hidden;
}

th, td {
  padding: 12px 15px;
  text-align: center;
}

th {
  background-color: #f2f2f2;
  font-weight: bold;
}

tr {
  transition: background-color 0.3s ease;
}

tr:nth-child(even) {
  background-color: #f9f9f9;
}

tr:hover {
  background-color: #f1f1f1;
}

button {
  cursor: pointer;
  padding: 5px 10px;
  background-color: cornflowerblue;
  color: white;
  border: none;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #6495ed;
}
</style>