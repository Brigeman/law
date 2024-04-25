import React, { useState } from 'react';
import './Navbar.css';

function Navbar() {
  const [indicatorStyle, setIndicatorStyle] = useState({});

  const handleMouseMove = (e) => {
    const link = e.target;
    const linkRect = link.getBoundingClientRect();
    setIndicatorStyle({
      left: `${linkRect.left + window.scrollX}px`,
      top: `${linkRect.bottom + window.scrollY - 5}px`,
      width: `${linkRect.width}px`,
      height: '5px',
      borderRadius: '50%',
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
        {['Услуги', 'Портфолио', 'Команда', 'Отзывы', 'Я требую авокадо', 'Контакты'].map((text, index) => (
          <li key={index} className="nav-item" onMouseOut={handleMouseOut}>
            <a href={`/${text.toLowerCase()}`} onMouseMove={handleMouseMove} className="bodoni-moda-nav">{text}</a>
          </li>
        ))}
      </ul>
      <div className="nav-indicator" style={indicatorStyle} />
    </nav>
  );
}

export default Navbar;
