import React, { useEffect, useState } from 'react';
import { apiClient } from '../../config/api';
import styles from './Services.module.css';

function Services() {
    const [services, setServices] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        apiClient.get('/services/')
        .then(response => {
            setServices(response.data);
            setLoading(false);
        })
        .catch(error => {
            console.error('Ошибка при загрузке услуг:', error);
            setError('Не удалось загрузить услуги');
            setLoading(false);
        });
    }, [])


return (
    <div className={styles.servicesContainer}>
      {loading && <p>Загрузка услуг...</p>}
      {error && <p style={{color: 'red'}}>{error}</p>}
      {!loading && !error && services.map(service => (
        <div className={styles.serviceCard} key={service.id}>
          <h2>{service.name}</h2>
          <p>{service.description}</p>
        </div>
      ))}
    </div>
  );
}

export default Services;