import { Component } from '@angular/core';
import { FormGroup,FormControl,Validators, AbstractControl} from '@angular/forms';







@Component({
  selector: 'app-project',
  templateUrl: './project.component.html',
  styleUrls: ['./project.component.css']
})
export class ProjectComponent {
  title="Product form"
  pform = new FormGroup({
  pid: new FormControl(null, [Validators.required, this.productIdValidator]),
  pname: new FormControl('',[Validators.required,this.productNameValidator]),
  pdesc: new FormControl('',[Validators.required]),
  pprice : new FormControl('',[Validators.required]),
  pqty: new FormControl(),
  pavail:new FormControl(),
  pimage:new FormControl()
    
  })
  
  submitReg(){
    console.log(this.pform.value)
  }
  productIdValidator(control: AbstractControl): { [key: string]: boolean } | null {
    const value = control.value;
  
    if (value !== null && value >= 1 && Math.floor(value) === value) {
      return null; // It's a valid product id
    } else {
      return { 'productIdInvalid': true }; // Invalid product id
    }
  }
  
  
  productNameValidator(control: AbstractControl): { [key: string]: boolean } | null {
    const value = control.value;
  
    if (/^[a-zA-Z\s]*$/.test(value)) {
      return null; // It's a valid product name
    } else {
      return { 'productNameInvalid': true }; // Invalid product name
    }
  }

 

}