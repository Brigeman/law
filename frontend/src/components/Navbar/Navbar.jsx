import React from 'react';
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
          <li><a href="http://localhost:3000/">Home</a></li>
          <li><a href="http://localhost:3000/">About</a></li>
          <li><a href="http://localhost:3000/">Services</a></li>
          <li><a href="http://localhost:3000/">Gallery</a></li>
          <li><a href="http://localhost:3000/">Feedback</a></li>
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
