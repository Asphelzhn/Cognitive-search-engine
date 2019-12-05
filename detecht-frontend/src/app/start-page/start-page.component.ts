import { Component, OnInit } from '@angular/core';
import {GetAnalyticsService} from '../network-services/get-analytics.service';
import {SearchService} from '../network-services/search.service';

@Component({
  selector: 'app-start-page',
  templateUrl: './start-page.component.html',
  styleUrls: ['./start-page.component.scss']
})
export class StartPageComponent implements OnInit {

  constructor(private searchService: SearchService) { }

  ngOnInit() {
    this.searchService.search('');
  }

}
