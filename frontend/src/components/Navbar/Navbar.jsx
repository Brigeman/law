import React, { useRef } from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
  const checkboxRef = useRef(null);

  const handleCloseMenu = () => {
    if (checkboxRef.current) {
      checkboxRef.current.checked = false;
    }
  };

  return (
    <React.Fragment>
      <input type="checkbox" id="active" ref={checkboxRef} />
      <label htmlFor="active" className="menu-btn_nav" aria-label="Open Menu">
        <span></span>
      </label>
      <div className="wrapper_nav">
        <label htmlFor="active" className="close_nav"></label>
        <div className="close-menu-btn" onClick={handleCloseMenu} aria-label="Close Menu">
          <span></span>
        </div>
        <ul>
          <li><Link to="/" onClick={handleCloseMenu}>Главная страница</Link></li>
          <li><Link to="/about" onClick={handleCloseMenu}>О нас</Link></li>
          <li><Link to="/services" onClick={handleCloseMenu}>Услуги</Link></li>
          <li><Link to="/staff" onClick={handleCloseMenu}>Команда</Link></li>
        </ul>
      </div>
    </React.Fragment>
  );
};

export default Navbar;
