import { Component, OnInit } from '@angular/core';
import {SearchResponse} from '../../data-types';
import {SearchService} from '../../network-services/search.service';

@Component({
  selector: 'app-related-search-hits',
  templateUrl: './related-search-hits.component.html',
  styleUrls: ['./related-search-hits.component.scss']
})
export class RelatedSearchHitsComponent implements OnInit {

  results: SearchResponse[];

  constructor(private searchService: SearchService) { }

  ngOnInit() {
    this.searchService.searchResponse.subscribe(searchResult => this.results = searchResult);
  }


}