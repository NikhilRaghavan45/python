import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { Outlet } from 'react-router-dom';
import logo from '../Shared/Images/woman-clothes.png';
import './Sidebar.css';
import SareeComp from './SareeComp';
import LehengaComp from './LehengaComp';
import TopsComp from './TopsComp';
import JeansComp from './JeansComp';



const ProductDetails = () => <div>ProductDetails Content</div>;
const Logout = () => <div>Logout Content</div>;

const SidebarComp = () => {
  return (
    <Router>
      <div>
        {/* Container for both navigation bar and sidebar */}
        <div className="container-fluid">
          <div className="sidebar">
            <Link to="/" className="d-flex align-items-center text-decoration-none" activeClassName="active" exact>
              <img src={logo} alt="hugenerd" width="30" height="30" className="rounded-circle" />
              <span className="d-none d-sm-inline mx-1">Women's Cloth</span>
            </Link>
            <Link to="/saree" activeClassName="active">
              Saree
            </Link>
            <Link to="/lehenga" activeClassName="active">
              Leghenga
            </Link>
            <Link to="/jeans" activeClassName="active">
              Jeans
            </Link>
            <Link to="/tops" activeClassName="active">
              Tops
            </Link>
            <Link to="/productdetails" activeClassName="active">
              ProductDetails
            </Link>
            <Link to="/logout" activeClassName="active">
              Logout
            </Link>
          </div>
        </div>

        <div className="content">
          {/* Use Routes instead of Route */}
          <Routes>
            <Route path="/saree" element={<SareeComp />} />
            <Route path="/lehenga" element={<LehengaComp/>} />
            <Route path="/jeans" element={<JeansComp/>} />
            <Route path="/tops" element={<TopsComp/>} />
            <Route path="/productdetails" element={<ProductDetails />} />
            <Route path="/logout" element={<Logout />} />
          </Routes>
        </div>
        <Outlet/>
      </div>
    </Router>
  );
};

export default SidebarComp;
