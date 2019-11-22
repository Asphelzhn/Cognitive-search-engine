import {Component, NgModule, OnInit, Input} from '@angular/core';
import {MatSidenavModule} from '@angular/material/sidenav';
import {MatToolbarModule} from '@angular/material/toolbar'
import { Router } from '@angular/router';
import {SearchResponse} from '../data-types';
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

  constructor(private adminNavbarToPageService: AdminNavbarToPageService) { }

  ngOnInit() {
    this.adminNavbarToPageService.page.subscribe(page => this.page = page);
  }
  changePage(newPage: string): void {
    this.adminNavbarToPageService.changePage(newPage);
  }
}
