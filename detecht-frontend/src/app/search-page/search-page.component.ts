import {Component, OnInit, Input, ViewChild} from '@angular/core';
import {environment} from '../../environments/environment';
import {SearchResponse} from '../data-types';

@Component({
  selector: 'app-search-page',
  templateUrl: './search-page.component.html',
  styleUrls: ['./search-page.component.scss']
})
export class SearchPageComponent implements OnInit {
  staticUrl: string;
  @Input() result: SearchResponse;

  constructor(
  ) {
  }

  ngOnInit() {
    this.staticUrl = environment.staticUrl;
  }

}
