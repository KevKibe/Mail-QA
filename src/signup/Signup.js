import React from 'react'
import mailcartImage from './assets/img/mailcart.png';

function Signup() {
  return (
    <>
                <main>
                <div class="hero-img">
                    <img src={mailcartImage} alt="" className="no-shadow" />
                </div>
                <div class="signup-container">

                        <h1 class="txt-gradient">Scan through your emails effortlessly</h1>

                        <p class="txt-white"></p>
                        <a href="#" class="btn-gradient">Sign up with Google</a>
                        <a href="#" class="txt-gradient">Login Instead</a>

                </div>
        </main>
    </>
  )
}

export default Signup

