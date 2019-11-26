import {Component, NgModule, OnInit, Input} from '@angular/core';
import {AdminNavbarToPageService} from '../message-services/admin-navbar-to-page.service';


@Component({
  selector: 'app-admin-page',
  templateUrl: './admin-page.component.html',
  styleUrls: ['./admin-page.component.scss']
})

@NgModule({
  imports: [],
  declarations: []
})

export class AdminPageComponent implements OnInit {

  page: string;
  events: string[] = [];
  opened: boolean;
  analytics = '/assets/admin-page/account-circle-icon.png';
  upload = '/assets/admin-page/file-upload-icon-light.png';
  edit = '/assets/admin-page/border-color-icon-light.png';

  constructor(private adminNavbarToPageService: AdminNavbarToPageService) { }

  ngOnInit() {
    this.adminNavbarToPageService.page.subscribe(page => this.page = page);
  }
  changePage(newPage: string): void {
    this.adminNavbarToPageService.changePage(newPage);
    // author Hanna Börjesson
    if (newPage === 'edit') {
      this.analytics = 'assets/admin-page/account-circle-icon-light.png';
      this.upload = 'assets/admin-page/file-upload-icon-light.png';
      this.edit = 'assets/admin-page/border-color-icon.png';
    } else if (newPage === 'upload') {
      this.analytics = 'assets/admin-page/account-circle-icon-light.png';
      this.upload = 'assets/admin-page/file-upload-icon.png';
      this.edit = 'assets/admin-page/border-color-icon-light.png';
    } else if (newPage === 'analytics') {
      this.analytics = '/assets/admin-page/account-circle-icon.png';
      this.upload = 'assets/admin-page/file-upload-icon-light.png';
      this.edit = 'assets/admin-page/border-color-icon-light.png';
    }
  }
}

