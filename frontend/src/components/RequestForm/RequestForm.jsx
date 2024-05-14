import React, { useState } from 'react';
import axios from 'axios';
import styles from './RequestForm.module.css';

function RequestForm({ onSubmit }) {
  const [formData, setFormData] = useState({
    Имя: '',
    Телефон: '',
    Telegram: '',
    email: '',
    subject: '',
    description: ''
  });

  const [isFormVisible, setIsFormVisible] = useState(true); // Добавляем состояние для видимости формы

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({ ...prevState, [name]: value }));
    setActive(e.target, true);
  };

  const handleBlur = (e) => {
    setActive(e.target, false);
  };

  const setActive = (el, isActive) => {
    const formField = el.parentNode;
    if (isActive) {
      formField.classList.add(styles.active);
    } else {
      formField.classList.remove(styles.active);
      el.value === '' ? formField.classList.remove(styles.filled) : formField.classList.add(styles.filled);
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const { subject, description } = formData; // Извлечение только нужных полей
    try {
      const response = await axios.post('http://127.0.0.1:8000/requests/', { subject, description }, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      console.log('Data Submitted:', response.data);
      onSubmit(response.data);
      setIsFormVisible(false); // Скрыть форму после успешной отправки
    } catch (error) {
      console.error('Ошибка при отправке данных:', error.response?.data || error.message);
    }
  };

  return (
    isFormVisible ? (
      <div className={styles.container}>
        <h2 className={styles.title}>Оставьте заявку и мы свяжемся с вами в ближайшее время</h2>
        <p className={styles.description}>Заполните форму ниже, чтобы отправить заявку.</p>
        <form onSubmit={handleSubmit} className={styles.formContainer} noValidate>
          {Object.entries(formData).map(([key, value]) => (
            <div key={key} className={styles.formField}>
              <label htmlFor={key} className={styles.formFieldLabel}>{key.charAt(0).toUpperCase() + key.slice(1)}</label>
              <input
                id={key}
                name={key}
                type={key === "email" ? "email" : "text"}
                className={styles.inputField}
                value={value}
                onChange={handleInputChange}
                onBlur={handleBlur}
              />
            </div>
          ))}
          <div className={styles.buttonsContainer}>
            <button type="submit" className={styles.submitButton}>Отправить</button>
          </div>
        </form>
      </div>
    ) : (
      <div className={styles.successMessage}>Заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.</div>
    )
  );
}

export default RequestForm;
