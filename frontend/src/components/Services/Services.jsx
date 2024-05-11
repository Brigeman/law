import React, { useEffect, useState } from 'react';
import axios from 'axios';
import styles from './Services.module.css';

function Services() {
    const [services, setServices] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/services/') // сделать чет с этой хуйней
        .then(response => {
            setServices(response.data);
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
    }, [])


return (
    <div className={styles.servicesContainer}>
      {services.map(service => (
        <div className={styles.serviceCard} key={service.id}>
          <h2>{service.name}</h2>
          <p>{service.description}</p>
        </div>
      ))}
    </div>
  );
}

export default Services;