import React from 'react';
import './Navbar.css';

function Navbar() {
  return (
    <nav className="navbar">
      <ul className="navbar-nav">
        <li className="nav-item"><a href="/services">Услуги</a></li>
        <li className="nav-item"><a href="/about">О компании</a></li>
        <li className="nav-item"><a href="/lawyers">Наши юристы</a></li>
        <li className="nav-item"><a href="/reviews">Отзывы</a></li>
        <li className="nav-item"><a href="/news">Новости</a></li>
        <li className="nav-item"><a href="/contacts">Контакты</a></li>
      </ul>
    </nav>
  );
}

export default Navbar;