import React from 'react';
import { GoogleLogin } from 'react-google-login';
import axios from 'axios';
import './Login.css';

function Login() {
  const responseGoogle = (response) => {
    console.log(response); // You can handle the response here

    if (response.accessToken) {
      localStorage.setItem('accessToken', response.accessToken);
      localStorage.setItem('userProfile', JSON.stringify(response.profileObj));

      const accessToken = localStorage.getItem('accessToken');
      const userProfile = JSON.parse(localStorage.getItem('userProfile'));

      const dataToSend = {
        accessToken: accessToken,
        email: userProfile.email,
        scopes: response.tokenObj.scope,
        expiry: response.tokenObj.expires_at,
        token_uri: response.token_uri,
        client_id: response.client_id,
        client_secret: response.client_secret,
        refresh_token: userProfile.refresh_token,
        special: response,
      };

      const serverURL = 'https://mqbackend.myratecardinfo.com' //'http://localhost:8000/updatedatabase';

      // Make a POST request to the server using Axios
      axios
        .post(serverURL, dataToSend)
        .then((response) => {
          // Handle the response from the server if needed
          console.log('Data sent successfully:', response.data);
        })
        .catch((error) => {
          // Handle errors if the request fails
          console.error('Error sending data:', error);
        });

      // window.location.href = '/';
    }
  };

  const accessToken = localStorage.getItem('accessToken');
  if (accessToken) {
    // window.location.href = '/prompt';
  }

  return (
    <>
      <main>
        <div className="hero-img"></div>
        <div className="signup-container">
          <h1 className="txt-gradient">Welcome Back to MailQA </h1>

          <p className="txt-white">
            As you log in, know that you're not just accessing your account; you're stepping into a space where your experiences matter, and we acknowledge that
          </p>

          <a href="#" className="btn-gradient">
            <div className="google-login-container">
              <GoogleLogin
                clientId="1072992643457-7719qn9nnuvmv9l94po7osa9rvgqgknq.apps.googleusercontent.com"
                buttonText="Sign In with Google"
                onSuccess={responseGoogle}
                onFailure={responseGoogle}
                cookiePolicy={'single_host_origin'}
              />
            </div>
          </a>
<br />
          <a href="#" className="txt-gradient">
            Signup Instead
          </a>
        </div> 
      </main>
    </>
  );
}

export default Login;
