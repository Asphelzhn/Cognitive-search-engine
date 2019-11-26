import {Component, NgModule, OnInit, Input} from '@angular/core';
import {MatSidenavModule} from '@angular/material/sidenav';
import {MatToolbarModule} from '@angular/material/toolbar'
import { Router } from '@angular/router';
import {SearchResponse} from '../data-types';
import {AdminNavbarToPageService} from '../message-services/admin-navbar-to-page.service';
import {style} from '@angular/animations';

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
  edit = '/assets/admin-page/ic_border_color_24_lightpx@2x.png';

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
      this.edit = 'assets/admin-page/ic_border_color_24_lightpx@2x.png';
    } else if (newPage === 'analytics') {
      this.analytics = '/assets/admin-page/account-circle-icon.png';
      this.upload = 'assets/admin-page/file-upload-icon-light.png';
      this.edit = 'assets/admin-page/ic_border_color_24_lightpx@2x.png';
    }
  }
}

