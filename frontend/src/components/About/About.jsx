import React, { useEffect, useState } from "react";
import { apiClient } from '../../config/api';
import styles from './About.module.css';

function About() {
    const [about, setAbout] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        apiClient.get('/about/')
        .then(response => {
            setAbout(response.data);
            setLoading(false);
        })
        .catch(error => {
            console.error('Ошибка при загрузке информации:', error);
            setError('Не удалось загрузить информацию');
            setLoading(false);
        });
    }, []);

    return (
        <div className={styles.aboutContainers}>
            {loading && <p>Загрузка информации...</p>}
            {error && <p style={{color: 'red'}}>{error}</p>}
            {!loading && !error && about.map(aboutItem => (
                <div className={styles.aboutCard} key={aboutItem.id}>
                    <h2>{aboutItem.title}</h2>
                    <p>{aboutItem.description}</p> 
                </div>
            ))}
        </div>
    );
}

export default About;
