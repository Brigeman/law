import React from 'react';
import './Footer.css';

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-top">
        <div className="footer-logo">Holyshit</div>
        <div className="footer-slogan">Not guilty</div>
        <div className="footer-tagline">предварительные выводы неутешительны: ...</div>
      </div>
      <hr />
      <div className="footer-mid">
        <div className="footer-address">
          <span>НАШ АДРЕС</span>
          <span>г. Одинцово, пр. Будапештская, 40</span>
          <span>ЗАПИСЬ НА КОНСУЛЬТАЦИЮ</span>
          <span>+7 000 000 000</span>
        </div>
        <div className="footer-services">
          <span>УСЛУГИ</span>
          {/* Вставьте ссылки на ваши услуги */}
        </div>
        <div className="footer-question">
          <span>ВОПРОС ЮРИСТУ</span>
          {/* Вставьте форму или ссылку для вопросов */}
        </div>
      </div>
      <div className="footer-bottom">
        <div className="footer-triangle"></div>
        <div className="footer-rights">
          Все права защищены, 2023
          <a href="/privacy-policy">Политика обработки персональных данных</a>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
