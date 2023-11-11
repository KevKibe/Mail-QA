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
import emailCheckingVideo from '../assets/img/bg.gif';
import devicesImage from '../assets/img/devices.png';
import slackWorkspaceVideo from '../assets/img/email_checking.mp4';

function Home() { 
  return (
    <>
      <main>
        <div className="showcase">
          <p className="txt-gradient-light" data-aos="fade-up" data-aos-duration="1000" data-aos-delay="200">
            <TypeWriter
              words={["Scanning through emails was the old thing"]}
              wait={1000000}
            />
          </p>

          <small className="txt-white" data-aos="fade-up" data-aos-duration="800" data-aos-delay="700">
            AI powered tool that helps you manage your emails using natural language prompts
          </small>
          <a href="https://join.slack.com/t/digital-dynamos-group/shared_invite/zt-2609f7b1w-zVJylghjkdyDCucv_U~EXw" data-aos="fade-up" data-aos-duration="1000" data-aos-delay="1000" className="btn-gradient-blue">Get Started</a>
        </div>
      </main>

      <section>
        <h1 className="txt-gradient-light txt-light" data-aos="fade" data-aos-duration="1000">
          All Your answers at a <span className="txt-gradient">prompt</span>
        </h1>
        <div className="container">
          <div className="prompt-quiz" data-aos="fade-up" data-aos-duration="1000" data-aos-delay="200">
            <p className="user">U</p>
            <p className="quiz txt-gradient-light">
              <TypeWriter
                words={["Could I get a summary of all hackathon emails today"]}
                wait={1555500}
              />
            </p>
          </div>

          <div className="response" data-aos="flip-up" data-aos-duration="1000" data-aos-delay="800">
            <p className="gpt" data-aos="fade" data-aos-duration="1000" data-aos-delay="200"><img src="./assets/img/iconlogo.png" alt="" /></p>
            <p className="txt-gradient-light">
              <TypeWriter
                words={[
                  "Here is a summary of all emails with the keyword hackathon. Subject: Amazing Hackathon: On 12 NovSummary: The email highlights an upcoming hackathon scheduled for November 12th. It promises an exciting opportunity to showcase skills, collaborate, and solve real-world problems. The event emphasizes networking, prizes, and recognition. Recipients are encouraged to register, prepare, form teams, and get ready for a day of innovation. The sender expresses enthusiasm about the recipients potential contribution.Action Items:- Save the date: November 12th.- Register for the hackathon.- Prepare ideas and skills.- Consider forming or joining a team",
                ]}
                wait={155000}
              />
            </p>
          </div>
        </div>
        <a href="https://join.slack.com/t/digital-dynamos-group/shared_invite/zt-2609f7b1w-zVJylghjkdyDCucv_U~EXw" className="btn-gradient-blue try" data-aos="fade-right" data-aos-duration="1000" data-aos-delay="200">Give It a try</a>

      </section>

      <section>
      <h1 className="txt-gradient-light txt-light" data-aos="fade-up" data-aos-duration="1000" data-aos-delay="0">
        Also in your Slack workspace
      </h1>
      <video src={slackWorkspaceVideo} width="80%" autoPlay muted loop data-aos="zoom-out-up" data-aos-duration="1000" data-aos-delay="200"></video>
    </section>

      <section>
      <h1 className="txt-light txt-gradient-light" data-aos="zoom-in" data-aos-duration="1000" data-aos-delay="200">
        And That's Not All
      </h1>
      <div className="grid-container" data-aos="fade" data-aos-duration="100" data-aos-delay="20">
        <div className="grid-item" data-aos="fade-left" data-aos-duration="1000" data-aos-delay="200">
          <p className="txt-gradient">Retrieve information shared within the workspace</p>
        </div>
        <div className="grid-item" data-aos="fade-right" data-aos-duration="1000" data-aos-delay="200">
          <p className="txt-gradient">Obtain data accessible through Google searches.</p>
        </div>
        <div className="grid-item" data-aos="fade-right" data-aos-duration="1000" data-aos-delay="200">
          <p className="txt-gradient">Quickly find, compose and send emails</p>
        </div>
        <div className="grid-item" data-aos="fade-left" data-aos-duration="1000" data-aos-delay="200">
          <p className="txt-gradient">Schedule and track meetings and events</p>
        </div>
      </div>
      <a href="https://join.slack.com/t/digital-dynamos-group/shared_invite/zt-2609f7b1w-zVJylghjkdyDCucv_U~EXw" className="btn-gradient-blue" data-aos="fade-right" data-aos-duration="1000" data-aos-delay="200">
        Sign up now
      </a>
    </section>


      <section>
      <h1 className="txt-gradient-light txt-light" data-aos="fade" data-aos-duration="1000">
        Where do I use MailQA?
      </h1>
      <div className="grid" data-aos="zoom-in-up" data-aos-duration="1000" data-aos-delay="200">
        <img src={devicesImage} alt="" />
        <div className="text y-start x-start">
          <h1 className="txt-gradient-light">It runs on just about anything</h1>
          <small className="txt-white">
            MailQA is accessible on all devices and platforms from your smartphone to your laptop to your iPad.
          </small>
          <a href="https://join.slack.com/t/digital-dynamos-group/shared_invite/zt-2609f7b1w-zVJylghjkdyDCucv_U~EXw" className="btn-gradient-blue">
            Sign up now
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