import React, { useEffect, useState } from "react";
import { apiClient } from '../../config/api';
import styles from './Staff.module.css';

function Staff() {
    const [staff, setStaff] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        apiClient.get('/staff/')
        .then(response => {
            setStaff(response.data);
            setLoading(false);
        })
        .catch(error => {
            console.error('Ошибка при загрузке сотрудников:', error);
            setError('Не удалось загрузить сотрудников');
            setLoading(false);
        });
    }, []);

    return (
        <div className={styles.staffContainers}>
            {loading && <p>Загрузка сотрудников...</p>}
            {error && <p style={{color: 'red'}}>{error}</p>}
            {!loading && !error && staff.map(staff => (
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
