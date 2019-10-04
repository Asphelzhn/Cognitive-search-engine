import { Component, OnInit } from '@angular/core';
import {results} from '../../mock-results';
import {SearchResult} from '../../data_types';

@Component({
  selector: 'app-search-hits',
  templateUrl: './search-hits.component.html',
  styleUrls: ['./search-hits.component.scss']
})
export class SearchHitsComponent implements OnInit {

  result: SearchResult;
  results = results;

  constructor() { }

  ngOnInit() {
  }

}
