import { Component, OnInit } from '@angular/core';
import {AdminNavbarToPageService} from '../../message-services/admin-navbar-to-page.service';

@Component({
  selector: 'app-admin-navbar',
  templateUrl: './admin-navbar.component.html',
  styleUrls: ['./admin-navbar.component.scss']
})
export class AdminNavbarComponent implements OnInit {

  constructor(private adminNavbarToPageService: AdminNavbarToPageService) { }

  ngOnInit() {
  }

  changePage(newPage: string): void {
    this.adminNavbarToPageService.changePage(newPage);
  }

}
