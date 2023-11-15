import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './cloths.css'

const RegisterComp = () => {
   const[fname,setfname]=useState('');
  const[lname,setlname]=useState('');
  const[num,setnum]=useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  // const[Rpassword,setRPassword]=useState('');
  const [retypePassword, setRetypePassword] = useState('');
  const [valid, setValid] = useState(false);
   
 
    const handlePasswordChange = (e) => {
      setPassword(e.target.value);
      // Perform your password validation here
      validatePasswords(e.target.value, retypePassword);
    };
  
    const handleRetypePasswordChange = (e) => {
      setRetypePassword(e.target.value);
      // Perform your password validation here
      validatePasswords(password, e.target.value);
    };
  
    const validatePasswords = (password, retypePassword) => {
      // Check if passwords match and meet validation criteria
      if (password === retypePassword && password.length >= 8) {
        setValid(true);
      } else {
        setValid(false);
      }
    };
  const handleFirstName = (e) => {
    setfname(e.target.value);
  };
  const handleLastName = (e) => {
    setlname(e.target.value);
  };
  const handleContact = (e) => {
    setnum(e.target.value);
  };
  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };


  const handleSubmit = (e) => {
    e.preventDefault();
    // Perform form submission logic here
    if (valid) {
      // Submit the form or perform desired action
      console.log('Form submitted!');
    } else {
      console.log('Form not submitted. Please check passwords.');
    }
  };



  
  return (
    <div className="background-container">
    <div className="container ">
      <div className="row">
        <div className="col-4 mt-5">
        
            {/* <div className="card-body"> */} 
              <h2 className='mt-5 '>Sign Up</h2><br/>
              <form  onSubmit={handleSubmit}>

              <div className="col-8 mx-auto">
                  <label htmlFor="fname" className="form-label">First Name</label>
                  <input
                    type="text"
                    className="form-control border-danger"
                    id="fname"
                    value={fname} 
                    pattern="[A-Za-z]{3,10}"
                    onChange={handleFirstName}
                    required />
                   
                </div>
                <div className="col-8 mx-auto">
                <label htmlFor="email" className="form-label">Last Name</label>
                  <input
                    type="text"
                    className="form-control border-danger"
                    id="lname"
                    value={lname}
                    onChange={handleLastName}
                    />
                </div>
                <div className="col-8 mx-auto">
                  <label htmlFor="tel" className="form-label">Contact No</label>
                  <input
                    type="tel"
                    className="form-control border-danger"
                    id="tel"
                    value={num}
                    pattern="[789][0-9]{9}" 
                    onChange={handleContact}
                    required
                  />
                </div>
                <div className="col-8 mx-auto">
                  <label htmlFor="email" className="form-label">Email:</label>
                  <input
                    type="email"
                    className="form-control border-danger"
                    id="email"
                    value={email}
                    onChange={handleEmailChange}
                    required
                  />
                </div>
                <div className="col-8 mx-auto">
                  <label htmlFor="password" className="form-label">Password:</label>
                  <input
                    type="password"
                    className="form-control border-danger"
                    id="password"
                    pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"
                    value={password}
                    onChange={handlePasswordChange}
                    required
                  />
                </div>
                <div className="col-8 mx-auto">
                  <label htmlFor="retypePassword" className="form-label">Re-Type Password:</label>
                  <input
                    type="password"
                    className="form-control border-danger"
                    id="Retypepassword"
                    value={retypePassword}
                    onChange={handleRetypePasswordChange}
                    required
                />
                  {/* {valid ? <p className='text-danger'>Passwords match and meet criteria</p> : <p>Passwords do not match or do not meet criteria</p>} */}
                </div><br/>
                <button type="submit" className="btn btn-primary ml-1"  disabled={!valid}>Sign In</button>
              
               
              </form>
            </div>
          </div>
        </div>
      </div>
    // </div>
    // </div>
  );
};

export default RegisterComp;