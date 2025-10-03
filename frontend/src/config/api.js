import axios from 'axios';

// Base API URL - автоматически определяется по окружению
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:8000';

// Создаем экземпляр axios с базовой конфигурацией
const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000, // 10 секунд таймаут
  headers: {
    'Content-Type': 'application/json',
  },
});

// Интерцептор для обработки ошибок
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

// Экспортируем готовые методы для API
export const apiClient = {
  // GET запросы
  get: (url, config = {}) => api.get(url, config),
  
  // POST запросы
  post: (url, data = {}, config = {}) => api.post(url, data, config),
  
  // PUT запросы
  put: (url, data = {}, config = {}) => api.put(url, data, config),
  
  // DELETE запросы
  delete: (url, config = {}) => api.delete(url, config),
};

// Экспортируем базовый URL для использования в других местах
export { API_BASE_URL };

export default api;
