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
    // Redirect or handle the case where the user is already authenticated
    // window.location.href = '/prompt';
  }

  return (
    <>
      <section>
        <div className="auth-container" data-aos="flip-left" data-aos-duration="1000" data-aos-delay="0">
          <h1 className="txt-gradient-light txt-center">It's great to have you back</h1>
          <p className="txt-gradient-light txt-center">
            As You Log In, Know That You're Not Just Accessing Your Account; You're Stepping Into A Space Where Your
            Experiences Matter, And We Acknowledge That
          </p>
          <center>
          <GoogleLogin
            clientId="YOUR_GOOGLE_CLIENT_ID"
            buttonText="Login with Google"
            onSuccess={responseGoogle}
            onFailure={responseGoogle} // You can handle failures here
            cookiePolicy={'single_host_origin'}
          />
          </center>
        </div>
      </section>

      <script src="../assets/js/scroll_min.js"></script>

      <script>{`
        AOS.init();
      `}</script>
    </>
  );
}

export default Login;
