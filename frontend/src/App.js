import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header/Header';
import Footer from './components/Footer/Footer';
import Body from './components/Body/Body';
import Services from './components/Services/Services';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Routes>
          <Route path="/" element={<Body />} />
          <Route path="/services" element={<Services />} />
          {/* Добавить другие маршруты здесь при необходимости */}
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
