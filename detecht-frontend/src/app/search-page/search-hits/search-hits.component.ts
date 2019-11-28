
import {Component, Input, OnInit} from '@angular/core';
import {SearchResponse, Spellcheck} from '../../data-types';
import {SearchService} from '../../network-services/search.service';
import {environment} from '../../../environments/environment';


@Component({
  selector: 'app-search-hits',
  templateUrl: './search-hits.component.html',
  styleUrls: ['./search-hits.component.scss']
})
export class SearchHitsComponent implements OnInit {

  results: SearchResponse[];
  staticUrl: string;
  numberOfHits: number;
  @Input() result: SearchResponse;
  counter: number;

  constructor(
    private searchService: SearchService,
  ) {
  }

  ngOnInit() {
    this.staticUrl = environment.staticUrl;
    this.searchService.searchResponse.subscribe(searchResult => this.results = searchResult);
    this.searchService.totalResults.subscribe(totalResults => this.numberOfHits = totalResults);
  }

  removeResult(title: string) {
    this.counter = 0;
    for (const result of this.results) {
      if (result.title === title) {
        this.results.splice(this.counter, 1);
      }
      this.counter = + 1;
    }
  }
}

