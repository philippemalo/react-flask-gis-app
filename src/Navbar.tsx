import React from 'react'
import { Link } from 'react-router-dom'
import { NavbarContainer } from './styles/NavbarContainer.css'
import mainIcon from './svgs/mainIcon.svg'

export const Navbar = () => {
  return (
    <NavbarContainer>
        <Link className="App-link" to="/">
            <img src={mainIcon} alt="SVG as an image"></img>
        </Link>
        &nbsp;|&nbsp;
        <Link className="App-link" to="/page2">Page 2</Link>
    </NavbarContainer>
  )
}
