import React from 'react'
import logoImage from '../assets/img/logo.png';
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
            {accessToken ? 
                (
                    <li>
                        <a>MailQA</a>
                    </li>
                )
                :
            (
                <>
                                <li>
                    <a href="/signup">Signup <span>/</span></a>
                  </li>
                <li>
                <a href="/login">Login</a>
              </li>
                </>
            )
}

          </ul>
        </nav>
      </header>
    </>
  )
}

export default Header