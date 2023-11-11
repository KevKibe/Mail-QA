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
import slackWorkspaceVideo from '../assets/img/email_sending.mp4';
import slackWorkspaceVideo2 from '../assets/img/schedule meeting.mp4';
import previewImage from '../assets/img/preview.png';
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
      <h1 class="txt-gradient-light txt-light" data-aos="fade-up" data-aos-duration="1000" data-aos-delay="0"> <span class="txt-gradient">Use natural prompts to</span> Compose and send Emails </h1>
      <video src={slackWorkspaceVideo} width="80%" autoPlay muted loop data-aos="zoom-out-up" data-aos-duration="1000" data-aos-delay="200"></video>
    </section>
<br /><br />
    <section>
    <h1 class="txt-gradient-light txt-light" data-aos="fade-left" data-aos-duration="1000" data-aos-delay="0">  Schedule Meetings and Events </h1>
      <video src={slackWorkspaceVideo2} width="80%" autoPlay muted loop data-aos="zoom-out-up" data-aos-duration="1000" data-aos-delay="200"></video>
    </section>
<br />
<br />
      <section>
      <h1 class="txt-light txt-gradient-light" data-aos="zoom-in" data-aos-duration="1000" data-aos-delay="200">In a nutshell</h1>

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
    <section>
                <h1 class="txt-gradient-light txt-light" data-aos="fade" data-aos-duration="1000">Still to Come</h1>

                <div class="grid" data-aos="flip-left" data-aos-duration="1000" data-aos-delay="200">

                        <div class="text y-start x-start ">
                                <h1 class="txt-gradient-light">
                                        We're coming to other workspaces too
                                </h1>
                                <a href="#" class="btn-gradient-blue">Get Started</a>
                        </div>
                        <img src={previewImage} alt="Image Preview" />

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