import { Component, OnInit } from '@angular/core';
import {SearchService} from '../network-services/search.service';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.scss']
})
export class SearchBarComponent implements OnInit {

  constructor(private searchService: SearchService) { }

  private searchString: string;

  ngOnInit() {
  }

  search(): void {
    console.log('Searching for: ' + this.searchString);
    this.searchService.search(this.searchString);
  }

}
