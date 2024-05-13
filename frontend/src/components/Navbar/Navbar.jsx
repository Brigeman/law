import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
  return (
    <React.Fragment>
      <link href="https://fonts.googleapis.com/css2?family=Oswald&display=swap" rel="stylesheet" />
      <link href="https://fonts.googleapis.com/css2?family=Lato&display=swap" rel="stylesheet" />
      <script src="https://kit.fontawesome.com/a076d05399.js"></script>
      <input type="checkbox" id="active" />
      <label htmlFor="active" className="menu-btn_nav"><span></span></label>
      <div className="wrapper_nav">
        <label htmlFor="active" className="close_nav"></label>
        <div className="close-menu-btn" onClick={() => { document.getElementById('active').checked = false; }}>
          <span></span>
        </div>
        <ul>
          <li><Link to="/">Главная страница</Link></li>
          <li><Link to="/about">О нас</Link></li>
          <li><Link to="/services">Услуги</Link></li>
          <li><Link to="/staff">Команда</Link></li>
          <li><Link to="/feedback">Feedback</Link></li>
        </ul>
      </div>
    </React.Fragment>
  );
}

export default Navbar;
