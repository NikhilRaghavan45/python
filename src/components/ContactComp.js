import React, { useState } from 'react'
import './Contact.css'
import '/node_modules/bootstrap/dist/css/bootstrap.min.css'





const ContactComp = () => {
    const [fname, setfname] = useState('');
    const [email, setEmail] = useState('');
    const [num, setnum] = useState('');
    const [error, setError] = useState('');
    const [message, setMessage] = useState('');


    const handleFirstName = (e) => {
        setfname(e.target.value);
    };

    const handleContact = (e) => {
        setnum(e.target.value);
    };
    const handleEmailChange = (e) => {
        setEmail(e.target.value);
    };

    const handleMessageChange = (e) => {
        setMessage(e.target.value);
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        if (!fname || !email || !num || !message) {
            setError('All fields are required');
            return;
        }


        console.log('Form submitted!');

        setError('');
    };


    return (
        <div>
            <div className="container">
                <div><h1>Contact Us</h1></div>
                <br />
                <div className='row col-12'>
                    <div className="col-6">
                        <form className="my-form" onSubmit={handleSubmit}>
                            <div class="form-group ">
                                <label for="fname">Name</label>
                                <input type="text" class="form-control" id="fname" value={fname} pattern="[A-Za-z]{3,10}" onChange={handleFirstName} placeholder="Name" />
                            </div>
                                          

                            <div class="form-group mt-3">
                                <label for="email ">Email Address</label>
                                <input type="email" class="form-control" id="email" value={email} onChange={handleEmailChange} placeholder="Email Address" />
                            </div>
                           

                            <div class="form-group mt-3">
                                <label for="tel">Contact</label>
                                <input type="tel" class="form-control" value={num} pattern="[789][0-9]{9}" onChange={handleContact} placeholder="contact" />
                            </div>
                           

                            <div class="form-group mt-3">
                                <label for="form-message">Email your Message</label>
                                <textarea class="form-control" id="form-message" value={message} onChange={handleMessageChange} placeholder="message"></textarea>
                            </div>
                    

                            <button class="btn btn-default" type="submit"  style={{ marginTop: 20 }}>Contact Us</button>
                        </form>
                    </div>
                    <div className='col-6'>
                        <div id="map-container-google-2" className="z-depth-1-half map-container">
                            <iframe src="https://maps.google.com/maps?q=chicago&t=&z=13&ie=UTF8&iwloc=&output=embed" frameborder="0"
                                style={{ border: 0, height: 300, width: 600 }} allowfullscreen title="Google Map of Chicago"></iframe>

                        </div>
                    </div>

                </div>
            </div>


        </div>
    )
}


export default ContactComp
