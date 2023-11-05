import React from 'react'
import { GoogleLogin } from 'react-google-login';

function Signup() {
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
        //window.location.href = '/prompt';
      }
  return (
    <>
        <main>
                <div class="hero-img">
                        
                </div>
                <div class="signup-container">

                        <h1 class="txt-gradient">Welcome to MailQA </h1>

                        <p class="txt-white">
                        <h1 class="txt-gradient">Scan through your emails effortlessly</h1> 
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
                        <a href="/login" class="txt-gradient">sign In Instead</a>

                </div>
        </main>
    </>
  )
}

export default Signup