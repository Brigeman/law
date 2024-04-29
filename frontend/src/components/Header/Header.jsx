import React, { useState } from 'react';
import Navbar from '../Navbar/Navbar';
import RequestForm from '../RequestForm/RequestForm';
import Modal from 'react-modal';
import './Header.css';

function Header() {
  const [modalIsOpen, setModalIsOpen] = useState(false);

  const openModal = () => setModalIsOpen(true);
  const closeModal = () => setModalIsOpen(false);

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
          <div className="fill-container"></div>
        </button>
      </div>
      <Modal isOpen={modalIsOpen} onRequestClose={closeModal} contentLabel="Форма заявки">
        <RequestForm onSubmit={handleFormSubmit} onClose={closeModal} />
      </Modal>
      <div className="lower-header">
        <div className="logo">Holyshittech</div>
        <Navbar />
      </div>
    </header>
  );
}

export default Header;
