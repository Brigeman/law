import React, { useEffect, useState } from "react";
import axios from 'axios';
import styles from './Staff.module.css';

function Staff() {
    const [staff, setStaff] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/staff/')
        .then(response => {
            setStaff(response.data);
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
    }, []);

    return (
        <div className={styles.staffContainers}>
            {staff.map(staff => (
                <div className={styles.staffCard} key={staff.id}>
                    <h2>{staff.name}</h2>
                    <p>{staff.role}</p>
                    <p>{staff.email}</p>
                </div>
            ))}
        </div>
    );
}

export default Staff;
