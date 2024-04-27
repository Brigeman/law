import React from 'react';
import Navbar from '../Navbar/Navbar';
import './Header.css';

function Header() {
  // Text to display
  const buttonText = "Заказать звонок";

  // Function to apply faulty-letter class to every third letter
  const styledText = (text) => {
    return (
      <span className='glowing-txt'>
        {text.split('').map((char, index) => (
          (index + 1) % 3 === 0
            ? <span className='faulty-letter' key={index}>{char}</span>
            : char
        ))}
      </span>
    );
  };

  return (
    <header className="header">
      <div className="upper-header">
        <div className="contacts">
          <div className="phone">+7 000 00 00</div>
          <div className="email">holyshit@yahoo.com</div>
        </div>
        <button className='glowing-btn'>
          {styledText(buttonText)}
        </button>
      </div>
      <div className="lower-header">
        <div className="logo">Holyshittech</div>
        <Navbar />
      </div>
    </header>
  );
}

export default Header;
