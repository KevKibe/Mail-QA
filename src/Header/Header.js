import React from 'react'
import logoImage from '../assets/img/logo.png';
import { NavLink } from 'react-router-dom';

function Header() {
    const accessToken = localStorage.getItem('accessToken');

  return (
    <>
    <header>
        <div class="logo">
            <img src={logoImage} alt="" />
        </div>

          <ul>
            <li>
              <a href="./" className='txt-gradient-light'>Home <span>/</span></a>
            </li>
            {accessToken ? (
    <li>
        <a>MailQA</a>
    </li>
) : (
    <>
        <li>
            <NavLink to="/signup" className='txt-gradient'>Signup</NavLink>
        </li>
        <li>
            <NavLink to="/login" className='txt-gradient-light'>Login</NavLink>
        </li>
    </>
)}


          </ul>
      </header>
    </>
  )
}

export default Header