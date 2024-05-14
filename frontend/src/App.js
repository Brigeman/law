import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header/Header';
import Footer from './components/Footer/Footer';
import Body from './components/Body/Body';
import Services from './components/Services/Services';
import Staff from './components/Staff/Staff';
import About from './components/About/About';
import './App.css';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <ToastContainer />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Body />} />
            <Route path="/services" element={<Services />} />
            <Route path="/staff" element={<Staff />} />
            <Route path="/about" element={<About />} />
            {/* Добавить другие маршруты здесь при необходимости */}
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
