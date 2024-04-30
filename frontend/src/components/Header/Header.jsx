import React, { useState } from 'react';
import Navbar from '../Navbar/Navbar';
import RequestForm from '../RequestForm/RequestForm';
import Modal from 'react-modal';
import './Header.css';

function Header() {
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [isActive, setIsActive] = useState(false); // Добавлено состояние isActive

  const openModal = () => setModalIsOpen(true);
  const closeModal = () => setModalIsOpen(false);
  const toggleMenu = () => {
    setIsActive(prevIsActive => {
      console.log('Toggle menu clicked. isActive will be:', !prevIsActive); // Покажет ожидаемое новое состояние
      return !prevIsActive;
    });
  };

  const handleFormSubmit = (phoneNumber) => {
    console.log('Заявка отправлена с номером:', phoneNumber);
  };

  return (
    <header className="header">
      <div className="upper-header">
        <div className="contacts">
          <div className="phone">+7 000 00 00</div>
          <div className="email">holyshit@yahoo.com</div>
        </div>
        <button className='request-btn' onClick={openModal}>
          <span className='button-text'>Оставить заявку</span>
        </button>
      </div>
      <Modal isOpen={modalIsOpen} onRequestClose={closeModal} contentLabel="Форма заявки">
        <RequestForm onSubmit={handleFormSubmit} onClose={closeModal} />
      </Modal>
      <div className="lower-header">
        <div className="logo">Holyshittech</div>
        <Navbar isActive={isActive} toggleMenu={toggleMenu} />
      </div>
    </header>
  );
}

export default Header;
