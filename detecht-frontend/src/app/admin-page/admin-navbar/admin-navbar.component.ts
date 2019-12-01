import { Component, OnInit } from '@angular/core';
import { AdminNavbarToPageService } from '../../message-services/admin-navbar-to-page.service';

@Component({
  selector: 'app-admin-navbar',
  templateUrl: './admin-navbar.component.html',
  styleUrls: ['./admin-navbar.component.scss']
})
export class AdminNavbarComponent implements OnInit {

  liked: boolean = false;

  constructor(private adminNavbarToPageService: AdminNavbarToPageService) { }

  ngOnInit() {

  }

  onSubmit() {
    //TODO: Fix service to log out admin
  }


  changePage(newPage: string): void {
    //this.liked = true;
    this.adminNavbarToPageService.changePage(newPage);
  }

}
