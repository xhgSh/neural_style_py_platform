import axios from 'axios';

const API_URL = 'http://localhost:5000';//Flask

//Axios
axios.defaults.withCredentials = true;

export const register = (data) => {
    return axios.post(`${API_URL}/register`, data);
};

export const login = (data) => {
    return axios.post(`${API_URL}/login`, data);
};

export const getUserInfo = () => {
    return axios.get(`${API_URL}/api/getUserInfo`).then(response => {
        return {
            name: response.data.name,
            email: response.data.email,
            id: response.data.user_id
        };
    });
};

export const updateUsername = (data) => {
    return axios.post(`${API_URL}/update/username`, data);
};

export const updatePassword = (data) => {
    return axios.post(`${API_URL}/update/password`, data);
};

export const logout = () => {
    return axios.post(`${API_URL}/logout`);
};

export const deleteAccount = () => {
    return axios.delete(`${API_URL}/delete/account`);
};


export const getUsers = () => {
    return axios.get(`${API_URL}/api/getUsers`).then(response => {
        return response.data;
    });
};

export const deleteUser = (userId) => {
    return axios.delete(`${API_URL}/api/deleteUser/${userId}`);
};

export const promoteToAdmin = (userId) => {
    return axios.post(`${API_URL}/api/promoteToAdmin`, { userId });
};

export const getUserHistory = () => {
    return axios.get(`${API_URL}/api/getUserHistory`).then(response => {
        return response.data;
    });
};