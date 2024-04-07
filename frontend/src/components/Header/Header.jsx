import React from 'react';
import Navbar from '../Navbar/Navbar';
import './Header.css';

function Header() {
  return (
    <header className="header">
      <div className="upper-header">
        <div className="contacts">
          <div className="phone">+7 000 00 00</div>
          <div className="email">holyshit@yahoo.com</div>
        </div>
      </div>
      <div className="lower-header">
        <div className="logo">Holyshittech</div>
        <Navbar />
        <button className="call-button">Заказать звонок</button>
      </div>
    </header>
  );
}

export default Header;
