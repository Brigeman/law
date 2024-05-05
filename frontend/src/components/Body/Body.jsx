import React, { useState, useEffect, useMemo } from 'react';
import { useInView } from 'react-intersection-observer';
import './Body.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faScaleUnbalanced, faBriefcase, faBuilding, faCoins, faBrain, faHandshake, faUserShield, faLock, faUniversalAccess } from '@fortawesome/free-solid-svg-icons';

function Body() {
  const services = useMemo(() => [
    {
      title: 'Корпоративное право',
      icon: faHandshake,
      description: 'Регистрация и ликвидация юридических лиц, слияния и поглощения, корпоративное управление.'
    },
    {
      title: 'Трудовое право',
      icon: faBriefcase,
      description: 'Консультации по трудовым вопросам, разрешение трудовых споров, оформление трудовых договоров.'
    },
    {
      title: 'Недвижимость и строительство',
      icon: faBuilding,
      description: 'Сделки с недвижимостью, земельное право, строительные разрешения и споры.'
    },
    {
      title: 'Представительство в суде',
      icon: faScaleUnbalanced,
      description: 'Представление интересов клиентов в судах по гражданским делам, таким как споры о собственности, наследственные дела, трудовые споры, взыскание задолженности.'
    },
    {
      title: 'Налоговое право',
      icon: faCoins,
      description: 'Налоговое планирование, споры с налоговыми органами, налоговые проверки.'
    },
    {
      title: 'Интеллектуальная собственность',
      icon: faBrain,
      description: 'Патенты и торговые марки, авторское право, споры о нарушении прав.'
    }
  ], []);

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
        <h2 className="slogan">Ваш юридический партнер в стратегических решениях.</h2>
      </div>

      <div className="feature-container" ref={featuresRef}>
        <div className={`feature ${visibleFeatures ? 'visible' : ''}`}>
          <div className="feature-icon"><FontAwesomeIcon icon={faUserShield} /></div>
          <h3 className="feature-title">Доверие</h3>
          <p className="feature-description">Мы строим взаимоотношения с клиентами на принципах открытости и честности, гарантируя конфиденциальность и защиту ваших интересов на каждом этапе сотрудничества.</p>
        </div>
        <div className={`feature ${visibleFeatures ? 'visible' : ''}`}>
          <div className="feature-icon"><FontAwesomeIcon icon={faLock} /></div>
          <h3 className="feature-title">Надежность</h3>
          <p className="feature-description">Наши юридические решения отличаются неизменной точностью и обоснованностью, обеспечивая стабильность и предсказуемость в ваших деловых операциях.</p>
        </div>
        <div className={`feature ${visibleFeatures ? 'visible' : ''}`}>
          <div className="feature-icon"><FontAwesomeIcon icon={faUniversalAccess} /></div>
          <h3 className="feature-title">Этика</h3>
          <p className="feature-description">Мы придерживаемся высоких моральных стандартов во всех аспектах нашей работы, обеспечивая соблюдение этических норм ведения бизнеса и юридической практики.</p>
        </div>
      </div>

      <div className="services-list" ref={servicesRef}>
        {services.map((service, index) => (
          <div className={`service ${visibleServices.includes(index) ? 'visible' : ''}`} key={index}>
            <div className="service-icon">
              <FontAwesomeIcon icon={service.icon} />
            </div>
            <h3 className="service-title">{service.title}</h3>
            <p className="service-description">{service.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Body;
