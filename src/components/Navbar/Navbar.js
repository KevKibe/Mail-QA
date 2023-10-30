import React, { useContext, useState, useEffect } from 'react';
import logo from '../../assets/img/logo.png';

function Navbar() {
  // Assume your authentication context provides a `isLoggedIn` property
  const isLoggedIn = localStorage.getItem('accessToken');
  const accessToken = isLoggedIn;
  const [userinfo, setUserinfo] = useState();

  useEffect(() => {
    //FETCH API
    // Make a request to the Google API to fetch user information
    fetch('https://www.googleapis.com/oauth2/v1/userinfo?alt=json', {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    })
      .then((response) => response.json())
      .then((data) => {
        // `data` contains user information, including the username
        console.log('User information:', data);
        setUserinfo(data);
        // You can access the username as data.email or data.name, depending on the response format
      })
      .catch((error) => {
        console.error('Error fetching user information:', error);
      });
    //FETCH API
  }, []);

  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <a className="navbar-brand" href="/">
        <img src={logo} alt="Mail QA" height="40" />
      </a>
      <button
        className="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span className="navbar-toggler-icon"></span>
      </button>
      <div className="collapse navbar-collapse" id="navbarNav">
        <ul className="navbar-nav ml-auto">
            <li className="nav-item">
              <a className="nav-link" href="https://join.slack.com/t/digital-dynamos-group/shared_invite/zt-2609f7b1w-zVJylghjkdyDCucv_U~EXw">
                Home
              </a>
            </li>
        </ul>
      </div>
    </nav>
  );
}

export default Navbar;
