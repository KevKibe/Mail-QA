import React from 'react'
import { GoogleLogin } from 'react-google-login';
import Header from '../Header/Header';
import './Login.css';
function Login() {
    const responseGoogle = (response) => {
        console.log(response); // You can handle the response here
    
        if (response.accessToken) {
          localStorage.setItem('accessToken', response.accessToken);
          localStorage.setItem('userProfile', JSON.stringify(response.profileObj));
          window.location.href = '/';
        }
      };
    
      const accessToken = localStorage.getItem('accessToken');
      if (accessToken) {
        //window.location.href = '/prompt';
      }
  return (
    <>
        <main>
                <div class="hero-img">
                        
                </div>
                <div class="signup-container">

                        <h1 class="txt-gradient">Welcome Back to MailQA </h1>

                        <p class="txt-white">
                                As you log in, know that you're not just accessing your account; you're stepping into a space where your experiences matter, and we acknowledge that
                        </p>
                        <a href="#" class="btn-gradient">                
<div class="google-login-container">
  <GoogleLogin
    clientId="992390497960-a6cuvp6kaf44en2v1ktu0r29hibj7bks.apps.googleusercontent.com"
    buttonText="Sign In with Google"
    onSuccess={responseGoogle}
    onFailure={responseGoogle}
    cookiePolicy={'single_host_origin'}
  />
</div>

                </a>
                        <a href="#" class="txt-gradient">signup Instead</a>

                </div>
        </main>
    </>
  )
}

export default Login