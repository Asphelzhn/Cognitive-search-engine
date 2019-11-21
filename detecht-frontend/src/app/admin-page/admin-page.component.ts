import {Component, NgModule, OnInit, Input} from '@angular/core';
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

  constructor(private adminNavbarToPageService: AdminNavbarToPageService) { }

  ngOnInit() {
    this.adminNavbarToPageService.page.subscribe(page => this.page = page);
  }
}
