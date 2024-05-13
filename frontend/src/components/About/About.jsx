import React, { useEffect, useState } from "react";
import axios from 'axios';
import styles from './About.module.css';

function About() {
    const [about, setAbout] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/about/')
        .then(response => {
            setAbout(response.data);
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
    }, []);

    return (
        <div className={styles.aboutContainers}>
            {about.map(aboutItem => ( // Изменено имя переменной в map для избежания путаницы
                <div className={styles.aboutCard} key={aboutItem.id}>
                    <h2>{aboutItem.name}</h2>
                    <p>{aboutItem.description}</p> 
                </div>
            ))}
        </div>
    );
}

export default About;
