import { Component, OnInit } from '@angular/core';
import {AdminLoginService} from '../../network-services/admin-login.service';
import {NetworkAdminLoginRequest} from '../../network-services/network-data-types';
import {Router} from '@angular/router';

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.scss']
})
export class LoginPageComponent implements OnInit {

  constructor(private adminLoginService: AdminLoginService, private router: Router) { }
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
    this.adminLoginService.adminLogin(this.loginData).subscribe(
      (response) => {
        this.adminLoginService.setCookie(response.user);
        this.router.navigateByUrl('/admin');
      },
      (error) => {
        this.errorMessage = 'Wrong user name or password';
      }
    );

  }



}
