// RequestForm.jsx
import React, { useState } from 'react';
import styles from './RequestForm.module.css'; 

function RequestForm({ onSubmit, onClose }) {
  const [phoneNumber, setPhoneNumber] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    onSubmit(phoneNumber);
    onClose();  // Закрыть форму после отправки
  };

  return (
    <form onSubmit={handleSubmit} className={styles.formContainer}>
      <label className={styles.inputLabel}>
        Введите ваш номер телефона:
        <input
          type="text"
          className={styles.inputField}
          value={phoneNumber}
          onChange={e => setPhoneNumber(e.target.value)}
          required
        />
      </label>
      <button type="submit" className={styles.submitButton}>Отправить</button>
      <button onClick={onClose} type="button" className={styles.cancelButton}>Закрыть</button>
    </form>
  );
}

export default RequestForm;
