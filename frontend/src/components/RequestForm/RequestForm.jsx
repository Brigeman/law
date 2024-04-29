import React, { useState } from 'react';
import styles from './RequestForm.module.css';

function RequestForm({ onSubmit }) {
  const [formData, setFormData] = useState({
    Имя: '',
    Телефон: '',
    Telegram: '',
    email: '',
    Предмет: '',
    Описание: ''
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({ ...prevState, [name]: value }));
    setActive(e.target, true);
  };

  const handleBlur = (e) => {
    setActive(e.target, false);
  }

  const setActive = (el, isActive) => {
    const formField = el.parentNode;
    if (isActive) {
      formField.classList.add(styles.active);
    } else {
      formField.classList.remove(styles.active);
      el.value === '' ? formField.classList.remove(styles.filled) : formField.classList.add(styles.filled);
    }
  }

  const handleSubmit = (event) => {
    event.preventDefault();
    onSubmit(formData);
    console.log('Data Submitted:', formData);
  };

  return (
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
  );
}

export default RequestForm;
