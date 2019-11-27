import { Component, OnInit } from '@angular/core';
import {GetAnalyticsService} from '../../../network-services/get-analytics.service';
import {NetworkGetAnalyticsResponse} from '../../../network-services/network-data-types';

@Component({
  selector: 'app-stats',
  templateUrl: './stats.component.html',
  styleUrls: ['./stats.component.scss']
})
export class StatsComponent implements OnInit {

  constructor(private interact: GetAnalyticsService) { }
  result: NetworkGetAnalyticsResponse;

  ngOnInit() {
    this.interact.getAnalytics().subscribe(
      response => this.result = response
    );
  }

}
