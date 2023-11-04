import React from 'react'
import TypeWriter from '../typing/type';

//image resources
import illImage from '../assets/img/ill-removebg-preview.png';
import iconLogoImage from '../assets/img/iconlogo.png';
import envelopeImage from '../assets/img/envelope.png';
import awsImage from '../assets/img/aws.png';
import oaImage from '../assets/img/oa.png'; 
import slackImage from '../assets/img/slack.png';
import supaImage from '../assets/img/supa.png';
import mtImage from '../assets/img/mt.png';


function Home() { 
  return (
    <>
    <main>
        <div className="hero-text"> 
        <p style={{
              color: 'white',
            }}>
                          <TypeWriter
              words={["Clicking Through Emails and Workspace Data Was The Old Thing."]}
              wait={1000000}
            />
            </p>

          <a href="https://join.slack.com/t/digital-dynamos-group/shared_invite/zt-2609f7b1w-zVJylghjkdyDCucv_U~EXw" className="btn-gradient">
            Get Started
          </a>
        </div>
        <div className="hero-img">
          <img src={illImage} alt="" />
        </div>
      </main>

        <section>
        <div
          className="prompt-container"
          data-aos="fade"
          data-aos-duration="1100"
          data-aos-delay="200"
          data-aos-easing="ease-in"
        >
          <div className="query">
            <div className="u">U</div>
            <p style={{
              color: 'white',
            }}>
              <TypeWriter
                words={["Summarize my unread emails"]}
                wait={1555500}
              />
            </p>
          </div>

          <div className="response">
            <img src={iconLogoImage} alt="" />
            <p style={{
              color: 'white',
            }}>
              <TypeWriter
                words={[
                  "Here is a summary \n\nSubject: You have an email confirming a scheduled meeting tomorrow, another email inviting you to a webinar by Google Africa and the last unread email an introduction by John Doe asking to collaborate on a project. The sender expresses enthusiasm about the potential contribution.\n\n",
                ]}
                wait={155000}
              />
            </p>

          </div>
        </div>

        <a
          href="https://join.slack.com/t/digital-dynamos-group/shared_invite/zt-2609f7b1w-zVJylghjkdyDCucv_U~EXw"
          className="btn-gradient"
          data-aos="fade"
          data-aos-duration="1000"
          data-aos-delay="20"
          data-aos-easing="ease-in"
        >
          Try it yourself
        </a>
        </section>


      <section className="numbers">
        <h2
          className="txt-gradient"
          data-aos="fade-up"
          data-aos-duration="1000"
          data-aos-delay="20"
          data-aos-easing="ease-in"
        >
          According to a study by Mckinsey
        </h2>
        <h1
          className="txt-white"
          data-aos="fade-up"
          data-aos-duration="1000"
          data-aos-delay="400"
          data-aos-easing="ease-in"
        >
          28 <span className="txt-gradient">%</span>
        </h1>
        <h3
          className="txt-gradient"
          data-aos="fade-up"
          data-aos-duration="800"
          data-aos-delay="450"
          data-aos-easing="ease-in"
        >
          Of work time is spent clicking through emails
        </h3>
      </section>

      <section className="showcase">
        <div className="grid-2">
          <img
            src={envelopeImage}
            data-aos="fade-left"
            data-aos-duration="800"
            data-aos-delay="60"
            data-aos-easing="ease-in"
            alt=""
            height="90%"
          />

          <div
            className="text"
            data-aos="fade-right"
            data-aos-duration="800"
            data-aos-delay="6"
            data-aos-easing="ease-in"
          >
            <h1 className="txt-gradient">
              Find What You Need and boost your productivity
            </h1>

            <p className="txt-white">
              Say goodbye to wasted hours and hello to a productivity boost that
              transforms the way you work. Reclaim your time and make the most
              out of every email.
            </p>

            <a href="./signup" className="btn-gradient">
              Register now
            </a>
          </div>
        </div>
      </section>

      <section className="partners" >
        <h1
          className="txt-gradient"
          data-aos="fade-up"
          data-aos-duration="800"
          data-aos-delay="6"
          data-aos-easing="ease-in"
        >
          Powered By
        </h1>

        <scrollAnimation
          className="partners-container"
          data-aos="fade"
          data-aos-duration="800"
          data-aos-delay="600"
          data-aos-easing="ease-in"
        >
          <img src={awsImage} alt="Amazon Web Services" style={{
  height:'100px',
  width: '100px'
}}/>
          <img src={oaImage} alt="Oai" style={{
  height:'100px',
  width: '100px'
}}/>
          <img src={slackImage} alt="Slack" style={{
  height:'100px',
  width: '100px'
}}/>
          <img src={supaImage} alt="Supa" style={{
  height:'100px',
  width: '100px'
}}/>
          <img src={mtImage} alt="Mit" style={{
  height:'100px',
  width: '100px'
}}/>
        </scrollAnimation>
      </section>

      <script src="./assets/js/type.js"></script>
      <script src="./assets/js/scroll_min.js"></script>
      <script>
                AOS.init();
        </script>
    </>
  )
}

export default Home