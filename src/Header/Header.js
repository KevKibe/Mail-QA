import React from 'react'
import logoImage from '../assets/img/logo.png';
import { NavLink } from 'react-router-dom';

function Header() {
    const accessToken = localStorage.getItem('accessToken');

  return (
    <>
    <header>
        <img src={logoImage} alt="" />
        <nav>
          <ul>
            <li>
              <a href="./">Home <span>/</span></a>
            </li>
            {accessToken ? (
    <li>
        <a>MailQA</a>
    </li>
) : (
    <>
        <li>
            <NavLink to="/signup">Signup</NavLink>
        </li>
        <li>
            <NavLink to="/login">Login</NavLink>
        </li>
    </>
)}


          </ul>
        </nav>
      </header>
    </>
  )
}

export default Header