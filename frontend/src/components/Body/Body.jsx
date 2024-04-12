import React, { useState, useEffect } from 'react'; // Импортируем useEffect
import { useInView } from 'react-intersection-observer';
import './Body.css';

function Body() {
  // eslint-disable-next-line react-hooks/exhaustive-deps
  const services = [
    {
      title: 'Консультация',
      icon: '💬',
      description: 'Получите профессиональную юридическую консультацию.',
    },
    {
      title: 'Представительство в суде',
      icon: '⚖️',
      description: 'Полное представительство ваших интересов в судебных инстанциях.',
    },
    {
      title: 'Юридическое сопровождение',
      icon: '📜',
      description: 'Сопровождение сделок и юридических процедур.',
    },
    {
      title: 'Регистрация прав',
      icon: '🖊️',
      description: 'Регистрация прав на недвижимость и другое имущество.',
    },
    {
      title: 'Защита прав потребителей',
      icon: '🛡️',
      description: 'Юридическая помощь в защите прав потребителей.',
    },
    {
      title: 'Интеллектуальная собственность',
      icon: '🧠',
      description: 'Защита прав на интеллектуальную собственность и авторское право.',
    }
  ];
  const [visibleServices, setVisibleServices] = useState([]);
  const [visibleFeatures, setVisibleFeatures] = useState(false); 

  const { ref: servicesRef, inView: servicesInView } = useInView({
    triggerOnce: true,
    threshold: 1.0,
  });

  const { ref: featuresRef, inView: featuresInView } = useInView({
    triggerOnce: true,
    threshold: 1.0,
  });

  useEffect(() => {
    if (servicesInView) {
      setVisibleServices(services.map((_, index) => index));
    }
  }, [servicesInView, services]);

  useEffect(() => {
    if (featuresInView) {
      setVisibleFeatures(true); 
    }
  }, [featuresInView]);

  return (
    <div className="body-container">
      <div className="slogan-section">
        <h2 className="slogan">Ваш Слоган Здесь</h2>
        <button className="action-button">Нажми на Меня</button>
      </div>

      <div className="feature-container" ref={featuresRef}>
        <div className={`feature ${visibleFeatures ? 'visible' : ''}`}>
          <div className="feature-icon">🌟</div>
          <h3 className="feature-title">Доверие</h3>
          <p className="feature-description">Описание 1.</p>
        </div>
        <div className={`feature ${visibleFeatures ? 'visible' : ''}`}>
          <div className="feature-icon">🌟</div>
          <h3 className="feature-title">Надежность</h3>
          <p className="feature-description">Описание 2.</p>
        </div>
        <div className={`feature ${visibleFeatures ? 'visible' : ''}`}>
          <div className="feature-icon">🌟</div>
          <h3 className="feature-title">Этика</h3>
          <p className="feature-description">Описание 3.</p>
        </div>
      </div>

      <div className="services-list" ref={servicesRef}>
        {services.map((service, index) => (
          <div className={`service ${visibleServices.includes(index) ? 'visible' : ''}`} key={index}>
            <div className="service-icon">{service.icon}</div>
            <h3 className="service-title">{service.title}</h3>
            <p className="service-description">{service.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Body;
