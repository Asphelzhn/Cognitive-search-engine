import {Component, NgModule, OnInit, Input} from '@angular/core';
import { Router } from '@angular/router';
import {SearchResponse} from '../data-types';

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
  results: SearchResponse;
  constructor(
     private router: Router
  ) { }

  ngOnInit() {
  }
}
