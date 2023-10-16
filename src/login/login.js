import React from 'react';
import { GoogleLogin } from 'react-google-login';

function Login() {
  const responseGoogle = (response) => {
    console.log(response); // You can handle the response here

    if (response.accessToken) {
      localStorage.setItem('accessToken', response.accessToken);
      localStorage.setItem('userProfile', JSON.stringify(response.profileObj));
      window.location.href = '/prompt';
    }
  };

  const accessToken = localStorage.getItem('accessToken');
  if (accessToken) {
    window.location.href = '/prompt';
  }

  return (
    <main>
      <div className="container">
        <div className="row justify-content-center">
          <div className="col-md-6">
            <div className="form-container shadow p-4">
              <h2 className="text-primary text-center mb-4">Welcome on board</h2>

              <div className="google-btn text-center">
                <GoogleLogin
                  clientId="965274681666-p08jm4et6g955b9fmm0jeirg410qcug4.apps.googleusercontent.com"
                  buttonText="Sign In with Google"
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

export default Login;
