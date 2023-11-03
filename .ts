import { Component } from '@angular/core';
import { FormGroup,FormControl,Validators} from '@angular/forms';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent {
  title="Registration Group"
  rform = new FormGroup({
  fname :new FormControl('',[Validators.required,Validators.minLength(6), Validators.maxLength(15)]),
  lname: new FormControl('',[Validators.required,Validators.minLength(6), Validators.maxLength(15),Validators.pattern("^[a-zA-Z]+$")]),
  email: new FormControl('',[Validators.email,Validators.required,Validators.pattern("[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$")]),
  gender : new FormControl('',[Validators.required]),
  isMarried: new FormControl(),
  address:new FormGroup({
    city: new FormControl(),
    street: new FormControl(),
    pincode:new FormControl(),
    country:new FormControl()
  })
    
  })
  
  get firstname(){
    return this.rform.get("fname")
  }

  submitReg(){
    console.log(this.rform.value)
  }

}

