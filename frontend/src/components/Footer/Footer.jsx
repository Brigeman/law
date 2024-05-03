import React from 'react';
import './Footer.css';

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-section footer-left">
        <div className="footer-logo">
          Holyshit
          <div className="footer-slogan">Not guilty</div>
          <div className="footer-tagline">Tag...</div>
        </div>
      </div>
      <div className="footer-section footer-center">
        <div className="footer-rights">
          Все права защищены, 2023<br/>
          <a href="/privacy-policy">Политика обработки персональных данных</a> {/* добавить политику */}
        </div>
      </div>
      <div className="footer-section footer-right">
        <ul className="social-media-links">
          <li><a href="https://www.instagram.com"><i className="fa-brands fa-instagram instagram"></i></a></li>
          <li><a href="https://www.telegram.org"><i className="fa-brands fa-telegram telegram"></i></a></li>
          <li><a href="https://www.twitter.com"><i className="fa-brands fa-twitter twitter"></i></a></li>
        </ul>
      </div>
    </footer>
  );
}

export default Footer;
