import { Component, OnInit } from '@angular/core';
import {results} from '../../mock-results';
import {result} from '../../result';

@Component({
  selector: 'app-search-hits',
  templateUrl: './search-hits.component.html',
  styleUrls: ['./search-hits.component.scss']
})
export class SearchHitsComponent implements OnInit {

  result = result;
  results = results;

  constructor() { }

  ngOnInit() {
  }

}
