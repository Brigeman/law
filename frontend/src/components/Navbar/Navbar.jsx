import React, { useState } from 'react';
import './Navbar.css';

function Navbar() {
  const [indicatorStyle, setIndicatorStyle] = useState({});

  const handleMouseMove = (e) => {
    const link = e.target; // Получаем непосредственно ссылку, а не li
    const linkRect = link.getBoundingClientRect();
    setIndicatorStyle({
      left: `${linkRect.left + window.scrollX}px`,
      top: `${linkRect.bottom + window.scrollY - 5}px`, // Немного выше нижней границы ссылки
      width: `${linkRect.width}px`, // Ширина равна ширине ссылки
      height: '5px', // Высота для подчёркивания
      borderRadius: '50%', // Изначально звезда круглая
      transition: 'height 0.2s ease, width 0.2s ease, border-radius 0.2s ease, left 0.2s ease, top 0.2s ease',
      transform: 'none',
      opacity: 1,
    });
  };

  const handleMouseOut = () => {
    setIndicatorStyle((prevStyle) => ({
      ...prevStyle,
      opacity: 0,
      transition: 'opacity 0.5s ease',
    }));
  };

  return (
    <nav className="navbar">
      <ul className="navbar-nav">
        {['Услуги', 'Всем пиздец, все виновны', 'Наши миньены', 'Отзывы', 'Я требую авoкадо', 'Контакты'].map((text, index) => (
          <li key={index} className="nav-item" onMouseOut={handleMouseOut}>
            <a href={`/${text.toLowerCase()}`} onMouseMove={handleMouseMove}>{text}</a>
          </li>
        ))}
      </ul>
      <div className="nav-indicator" style={indicatorStyle} />
    </nav>
  );
}

export default Navbar;
