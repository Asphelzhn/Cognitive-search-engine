import { Component, OnInit } from '@angular/core';
import { AdminNavbarToPageService } from '../../message-services/admin-navbar-to-page.service';
import {AdminLoginService} from '../../network-services/admin-login.service';
import {Router} from '@angular/router';
import {SearchService} from '../../network-services/search.service';

@Component({
  selector: 'app-admin-navbar',
  templateUrl: './admin-navbar.component.html',
  styleUrls: ['./admin-navbar.component.scss']
})
export class AdminNavbarComponent implements OnInit {

  constructor(private adminNavbarToPageService: AdminNavbarToPageService,
              private adminLoginService: AdminLoginService,
              private router: Router,
              private searchService: SearchService) { }
  currentPage: string;

  ngOnInit() {
    this.adminNavbarToPageService.page.subscribe(page => this.currentPage = page);
  }

  logout() {
    this.adminLoginService.setCookie(0);
    this.router.navigateByUrl('');
  }


  changePage(newPage: string): void {
    this.adminNavbarToPageService.changePage(newPage);
    this.searchService.search('');
  }

}
