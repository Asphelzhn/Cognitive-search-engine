import {Component, Input, OnInit} from '@angular/core';
import {Router} from '@angular/router';
import {SearchService} from '../../../network-services/search.service';
import {SearchResponse} from '../../../data-types';

@Component({
  selector: 'app-search-edit-doc',
  templateUrl: './search-edit-doc.component.html',
  styleUrls: ['./search-edit-doc.component.scss']
})
export class SearchEditDocComponent implements OnInit {

  constructor(private searchService: SearchService, private router: Router) {
  }
  results: SearchResponse[];
  numberOfHits: number;
  searchString: string;
  // @Input() changePage: boolean;
  @Input() result: SearchResponse;

  ngOnInit() {
    this.searchService.searchResponse.subscribe(searchResult => this.results = searchResult);
    this.searchService.totalResults.subscribe(totalResults => this.numberOfHits = totalResults);
    // this.searchService.currentSearch.subscribe(query => this.searchString = query);
  }

  search(): void {
    console.log('Searching for: ' + this.searchString);
    this.searchService.search(this.searchString);
  }
}
