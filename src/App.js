import React, { useEffect } from 'react';

//Libraries
import AOS from 'aos';
import 'aos/dist/aos.css';
import { gapi } from 'gapi-script';
import { BrowserRouter,Routes,Route } from 'react-router-dom';

//Style files
import './assets/css/_root.scss';
import './assets/css/style.scss';
import scrollAnimation from './animation/scrollAnimation';

//Screens
import Login from './Login/Login';
import Header from './Header/Header';
import Home from './Home/Home';
import Signup from './signup/Signup';

const App = () => {
  // Initialize AOS
  useEffect(() => {
    AOS.init();
  }, []);

  //Initialize Google Aunthetication
  useEffect(() => {
    function start() {
      gapi.client.init({
        clientId:'992390497960-a6cuvp6kaf44en2v1ktu0r29hibj7bks.apps.googleusercontent.com',
        scope:"https://www.googleapis.com/auth/gmail.readonly"
      });
    }

    gapi.load('client:auth2', start);
  }, []);
  return (
    <> 
      <BrowserRouter>
      <Header />
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<Signup />} />
            <Route path="/*" element={<Home />} />
          </Routes>
      </BrowserRouter>
    </>
  );
};

export default App;
