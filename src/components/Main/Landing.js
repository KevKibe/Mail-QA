import React from 'react';
import envelopeImage from '../../assets/img/envelope.png';
import mailcartImage from '../../assets/img/mailcart.png';
import scanImage from '../../assets/img/scan.png';

function Landing() {
  return (
    <div>
      <main>
        <div className="container">
          <div className="row">
            <div className="col-lg-6 d-flex align-items-center">
              <img src={envelopeImage} alt="" className="img-fluid" />
            </div>
            <div className="col-lg-6 d-flex align-items-center">
              <div className="text">
                <h1 className="txt-gradient txt-light">Scanning through emails was the old thing.</h1>
                <p className="txt-grey">
                  In a world where our inboxes are constantly inundated with messages from work, family, friends, and subscriptions, maintaining email sanity can be a daunting task. This is where we come in.
                </p>
                <a href="./signup" className="btn btn-primary">Sign up now</a>
              </div>
            </div>
          </div>
        </div>
      </main>

      <section>
        <div className="container">
          <div className="row">
            <div className="col-lg-6 d-flex align-items-center order-lg-2">
              <div className="text">
                <h1 className="txt-gradient txt-light">We are here to declutter your inbox</h1>
                <p className="txt-grey">
                  Our algorithm is dedicated to simplifying your digital life, providing you with the means to declutter, prioritize, and organize your emails effortlessly. Whether you're a busy professional, a student, or anyone seeking email tranquility, we're at your service.
                </p>
                <a href="./signup" className="btn btn-primary">Register now</a>
              </div>
            </div>
            <div className="col-lg-6 d-flex align-items-center order-lg-1">
              <img src={mailcartImage} alt="" className="img-fluid" />
            </div>
          </div>
        </div>
      </section>

      <section>
        <div className="container">
          <div className="row">
            <div className="col-lg-6 d-flex align-items-center">
              <img src={scanImage} alt="" className="img-fluid" />
            </div>
            <div className="col-lg-6 d-flex align-items-center">
              <div className="text">
                <h1 className="txt-gradient txt-light">Find What You Need and boost your productivity</h1>
                <p className="txt-grey">
                  Say goodbye to wasted hours and hello to a productivity boost that transforms the way you work. Reclaim your time and make the most out of every email.
                </p>
                <a href="./signup" className="btn btn-primary">Get started</a>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Landing;
