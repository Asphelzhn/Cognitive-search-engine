import { Component, OnInit } from '@angular/core';
import {SearchResponse} from '../../data-types';
import {SearchService} from '../../network-services/search.service';

@Component({
  selector: 'app-search-hits',
  templateUrl: './search-hits.component.html',
  styleUrls: ['./search-hits.component.scss']
})
export class SearchHitsComponent implements OnInit {

  results: SearchResponse[];

  constructor(private searchService: SearchService) { }

  ngOnInit() {
    this.searchService.searchResponse.subscribe(searchResult => this.results = searchResult);
  }

}

