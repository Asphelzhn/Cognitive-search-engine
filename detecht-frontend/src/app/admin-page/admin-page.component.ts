import {Component, NgModule, OnInit, Input} from '@angular/core';
import { Router } from '@angular/router';
import {SearchResponse} from '../data-types';
import {AdminNavbarToPageService} from '../message-services/admin-navbar-to-page.service';
import {AdminLoginService} from '../network-services/admin-login.service';
import {SearchService} from '../network-services/search.service';

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

  constructor(private adminNavbarToPageService: AdminNavbarToPageService,
              private adminLoginService: AdminLoginService,
              private router: Router) { }

  ngOnInit() {
    this.adminNavbarToPageService.page.subscribe(page => this.page = page);
    this.adminLoginService.userId.subscribe((id) => {
      // TODO change to 1
      if (id < 0) {
        this.router.navigateByUrl('');
      }
    });
  }
}
