import './assets/css/style.css';

import { BrowserRouter,Routes,Route } from 'react-router-dom';
import Navbar from './components/Navbar/Navbar';
import Landing from './components/Main/Landing';
import Login from './login/login';
import Signup from './signup/signup';
import Prompt from './components/prompt/Prompt';
import { useEffect } from 'react';
import { gapi } from 'gapi-script';

function App() {
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
      <Navbar /> 
      <BrowserRouter>
        <Routes>
            <Route path="/" element={<Landing />} />
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<Signup />} /> 
            <Route path="/prompt" element={<Prompt />} /> 
            <Route path="/*" element={<Landing />} />
          </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
