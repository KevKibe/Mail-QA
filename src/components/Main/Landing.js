import React from 'react';
import envelopeImage from '../../assets/img/envelope.png';
import mailcartImage from '../../assets/img/mailcart.png';
import scanImage from '../../assets/img/scan.png';
import iconLogo from '../../assets/img/iconlogo.png';
import awsImage from '../../assets/img/aws.png';
import oaImage from '../../assets/img/oa.png';
import slackImage from '../../assets/img/slack.png';
import supaImage from '../../assets/img/supa.png';
import mtImage from '../../assets/img/mt.png';
import "./Landing.css";

function Landing() { 
  const sectionStyle = {
    background: '#f5f5f5',
    padding: '20px',
    textAlign: 'center',
  };

  const containerStyle = {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'center',
  };

  const featureStyle = {
    maxWidth: '400px',
    margin: '10px',
    padding: '20px',
    background: 'white',
    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
    borderRadius: '8px',
  };

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
                <a href="./signup" className="btn btn-primary">Try it now</a>
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
                <a href="./signup" className="btn btn-primary">Try it now</a>
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
                <a href="./signup" className="btn btn-primary">Try it Now</a>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section style={sectionStyle}>
      <h2 style={{ fontSize: '24px', marginBottom: '20px' }}>
        Key Features
      </h2>

      <div style={containerStyle}>
        <div style={featureStyle}>
          <h3>Email Efficiency</h3>
          <p>
            Effortlessly locate specific emails in your inbox using natural
            language prompts.
          </p>
        </div>

        <div style={featureStyle}>
          <h3>Seamless Email Composing and Sending</h3>
          <p>
            Users can send emails directly from the app using just a natural
            language prompt.
          </p>
        </div>

        <div style={featureStyle}>
          <h3>Calendar Management</h3>
          <p>
            Users can schedule and track meetings and events using natural
            language prompts in the app.
          </p>
        </div>

        <div style={featureStyle}>
          <h3>Availability</h3>
          <p>
            Since our app is built as an integration on Slack, it is available on
            Web, Mobile, and Desktop.
          </p>
        </div>

        <div style={featureStyle}>
          <h3>Effortless Data Retrieval</h3>
          <p>
            Use natural language prompts to effortlessly access and extract data
            from any file format within your workspace, saving precious time and
            resources.
          </p>
        </div>
      </div>
    </section>
      <section className="partners">
        <h1 className="txt-gradient" data-aos="fade-up" data-aos-duration="800" data-aos-delay="6" data-aos-easing="ease-in">
          Powered By
        </h1>

        <div className="partners-container">
          <img src={awsImage} alt="" />
          <img src={oaImage} alt="" />
          <img src={slackImage} alt="" />
          <img src={supaImage} alt="" />
          <img src={mtImage} alt="" />
        </div>
      </section>
    </div>
  );
}

export default Landing;
