import { NavLink } from 'react-router-dom'
import React from 'react'
import './NavBar.css'

function NavBar(){
    return (
        <nav>
            <NavLink
                to = '/'
                className = 'nav-link'
            > Home
            </NavLink>
            <NavLink
                to = '/create_review'
                className = 'nav-link'
            > Create Review
            </NavLink>
        </nav>
    )
}

export default NavBar