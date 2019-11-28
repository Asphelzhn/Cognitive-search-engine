import { Component, OnInit } from '@angular/core';
import {AdminLoginService} from './network-services/admin-login.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'detecht-frontend';

  constructor(private adminLoginService: AdminLoginService) { }

  ngOnInit() {
    this.adminLoginService.checkLoggedIn();
  }
}
