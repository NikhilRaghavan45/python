
import React, { Component } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import NavComp from "./NavComp";
import HomeComp from "./HomeComp";
import MenuComp from "./MenuComp";
import AboutComp from "./AboutComp";
import ContactComp from "./ContactComp";
import FooterComp from "./FooterComp";
import LoginComp from "./LoginComp";
import RegisterComp from "./RegisterComp";
import BodyComp from "./BodyComp";






class MyRoutingComp extends Component {
    render() {
        return (
            <div>
                <BrowserRouter>

                    <div className="container-fluid">
                        <div className="card border">
                            <div className="card-header" style={{backgroundColor:'white'}}>
                                <NavComp />
                            </div>



                            <div className="card-body">
                               
                                <Routes>
                                    {/* default routing  */}
                                    <Route path="" element={<BodyComp/>}></Route>
                                    <Route path="HomeComp" element={<HomeComp />}></Route>
                                    <Route path="MenuComp" element={<MenuComp />}></Route>
                                    <Route path="AboutComp" element={<AboutComp />}></Route>
                                    <Route path="ContactComp" element={<ContactComp />}></Route>
                                    <Route path="LoginComp" element={<LoginComp />}></Route>
                                    <Route path="RegisterComp" element={<RegisterComp/>}></Route>
                                
                                </Routes>
                            </div>

                            <div className="card-footer">
                                <FooterComp/>
                            </div>
                           
                        </div>
                    </div>




                </BrowserRouter>
            </div>
        );
    }
}

export default MyRoutingComp;