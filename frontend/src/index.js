import React from 'react';
import ReactDOM from 'react-dom/client';
import './App.css';
import App from './App';
import Modal from 'react-modal';
import reportWebVitals from './reportWebVitals';

const rootElement = document.getElementById('root');
const root = ReactDOM.createRoot(rootElement);
Modal.setAppElement(rootElement); // Устанавливаем корневой элемент для react-modal

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
