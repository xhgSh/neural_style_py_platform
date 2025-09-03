<template>
  <div style="text-align: center; background-color: cornflowerblue; color: white; padding: 10px;">
    <h1 style="margin: 0; font-size: 24px;">Neural Style</h1>

  </div>
  <button @click="navigateToHome" style="background-color:darkgray; color:white; padding: 5px;">Back</button>
  <div id="history" style="display: flex; justify-content: center; align-items: center; height: 100vh; flex-direction: column;">
    <h1>History Page</h1>
    <div v-if="errorMessage">{{ errorMessage }}</div>
    <table v-if="history.length > 0">
      <thead>
        <tr>
          <th>Operation ID</th>
          <th>Content ID</th>
          <th>Style ID</th>
          <th>Time</th>
          <th>Delete</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="op in history" :key="op.id">
          <td>{{ op.id }}</td>
          <td>{{ op.content_id }}</td>
          <td>{{ op.style_id }}</td>
          <td>{{ op.time }}</td>
          <td>
            <button @click="deleteOperation(op.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { getUserHistory } from '../api';
import axios from 'axios';

export default {
  name: 'History',
  data() {
    return {
      history: [],
      errorMessage: ''
    };
  },
  methods: {
    async fetchHistory() {
      try {
        this.history = await getUserHistory();
      } catch (error) {
        console.error('Error fetching history:', error);
        this.errorMessage = 'Failed to fetch history';
      }
    },
    async deleteOperation(operationId) {
      try {
        await axios.delete(`http://localhost:5000/api/deleteOperation/${operationId}`);
        this.fetchHistory();
      } catch (error) {
        console.error('Error deleting operation:', error);
      }
    },
    navigateToHome() {
      this.$router.push('/home');
    }
  },
  mounted() {
    this.fetchHistory();
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