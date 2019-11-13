import {Component, Input, OnInit} from '@angular/core';
import {SearchResponse} from '../../data-types';
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
  @Input() result: SearchResponse;

  constructor(
    private searchService: SearchService,
  ) {
  }

  ngOnInit() {
    this.staticUrl = environment.staticUrl;
    this.searchService.searchResponse.subscribe(searchResult => this.results = searchResult);
  }

}

