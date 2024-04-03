import React, { useEffect, useState } from 'react';

function App() {
  const [clients, setClients] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/clients/')
      .then(response => response.json())
      .then(data => {
        console.log(data); // check
        setClients(data);
      })
      .catch(error => console.error("WTF:", error));
  }, []);

  return (
    <div>
      <h1>Clients</h1>
      {clients.map(client => (
        <div key={client.id}>{client.name}</div>
      ))}
    </div>
  );
}

export default App;
