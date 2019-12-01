import { Component, OnInit } from '@angular/core';
import { AdminNavbarToPageService } from '../../message-services/admin-navbar-to-page.service';
import {AdminLoginService} from '../../network-services/admin-login.service';

@Component({
  selector: 'app-admin-navbar',
  templateUrl: './admin-navbar.component.html',
  styleUrls: ['./admin-navbar.component.scss']
})
export class AdminNavbarComponent implements OnInit {

  constructor(private adminNavbarToPageService: AdminNavbarToPageService, private adminLoginService: AdminLoginService) { }
  currentPage: string;

  ngOnInit() {
    this.adminNavbarToPageService.page.subscribe(page => this.currentPage = page);
  }

  logout() {
    this.adminLoginService.setCookie(0);
  }


  changePage(newPage: string): void {
    this.adminNavbarToPageService.changePage(newPage);
  }

}
