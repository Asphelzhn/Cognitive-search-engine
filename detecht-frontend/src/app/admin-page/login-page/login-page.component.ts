import { Component, OnInit } from '@angular/core';
import {AdminLoginService} from '../../network-services/admin-login.service';
import {NetworkAdminLoginRequest} from '../../network-services/network-data-types';

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.scss']
})
export class LoginPageComponent implements OnInit {

  constructor(private adminLoginService: AdminLoginService) { }
  loginData: NetworkAdminLoginRequest;
  username: string;
  password: string;
  errorMessage: string;

  ngOnInit() {
  }

  onSubmit() {
    this.loginData = new NetworkAdminLoginRequest();
    this.loginData.username = this.username;
    this.loginData.password = this.password;
    console.log(this.loginData);
    this.adminLoginService.adminLogin(this.loginData).subscribe(
      (response) => {
        console.log('LoginResonse');
        console.log(response);
      },
      (error) => {
        this.errorMessage = 'Wrong user name or password';
        console.log(error);
      }
    );

  }



}
