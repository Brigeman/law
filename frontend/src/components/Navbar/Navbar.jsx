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
          <li><Link to="/">Home</Link></li>
          <li><Link to="/about">About</Link></li>
          <li><Link to="/services">Services</Link></li>
          <li><Link to="/gallery">Gallery</Link></li>
          <li><Link to="/feedback">Feedback</Link></li>
        </ul>
      </div>
      <div className="content_nav">
        <div className="title_nav">Fullscreen Overlay Navigation Bar</div>
        <p>(Hamburger Menu-2)</p>
      </div>
    </React.Fragment>
  );
}

export default Navbar;
