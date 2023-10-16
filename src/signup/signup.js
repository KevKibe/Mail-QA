import React from 'react';
import { GoogleLogin } from 'react-google-login';
import axios from 'axios';

function Signup() {
  const responseGoogle = (response) => {
    // Handle the user data received from Google OAuth
    const data = response.profileObj;

    console.log('Google user token:', response);
    console.log('Google user email:', data);

    axios.post('http://localhost:8000/updatedatabase', {
      accessToken: response.accessToken,
      email: data.email,
      client_id: '992390497960-a6cuvp6kaf44en2v1ktu0r29hibj7bks.apps.googleusercontent.com',
      client_secret: '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',
      token_uri: 'https://oauth2.googleapis.com/token',
      expiry: response.tokenObj.expires_in,
      refresh_token: response.tokenObj.access_token,
    });
    // You can send this user data to your server for registration/authentication.
  };

  return (
    <main>
      <div className="container">
        <div className="row justify-content-center">
          <div className="col-md-6">
            <div className="form-container shadow p-4 rounded">
              <h2 className="text-primary text-center mb-4">Welcome on board</h2>

              <div className="text-center">
                <GoogleLogin
                  clientId="992390497960-a6cuvp6kaf44en2v1ktu0r29hibj7bks.apps.googleusercontent.com"
                  buttonText="Sign up with Google"
                  onSuccess={responseGoogle}
                  onFailure={responseGoogle}
                  cookiePolicy={'single_host_origin'}
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}

export default Signup;
