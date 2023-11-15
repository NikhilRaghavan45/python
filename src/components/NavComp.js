import React, { Component } from 'react'
import '/node_modules/bootstrap/dist/css/bootstrap.min.css'
import './/External.css'
import { Link } from 'react-router-dom'
import logo from '../Shared/Images/woman-clothes.png'
import '/node_modules/bootstrap/dist/js/bootstrap.bundle.min.js'







class NavComp extends Component {
    render() {
        return (
            <div>
                <div className='container'>
                    <div className='Header'>
                        <img src={logo} alt='Women Cloth' width={40} height={40} style={{ float: 'left' }}></img>
                        <h3 style={{ float: 'left', marginLeft: 10 }}>Women's Cloth</h3>
                        <ul>

                            <Link to="HomeComp" className='btn'>Home</Link>
                            <Link to="MenuComp" className='btn'>Menu</Link>
                            <Link to="AboutComp" className='btn'>About</Link>
                            <Link to="ContactComp" className='btn'>Contacts</Link>
                            <li className="dropdown">
                                <Link
                                    to="#"
                                    className="btn dropdown-toggle"
                                    id="navbarDropdown"
                                    role="button"
                                    data-bs-toggle="dropdown"
                                    aria-haspopup="true"
                                    aria-expanded="false"
                                >
                                    My Account
                                </Link>
                                <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                                    <Link to="LoginComp" className="dropdown-item">
                                        Login
                                    </Link>
                                    <Link to="RegisterComp" className="dropdown-item">
                                        Register
                                    </Link>
                                </div>
                            </li>

                        </ul>
                    </div>

                </div>
            </div>
            


        )
    }
}

export default NavComp
