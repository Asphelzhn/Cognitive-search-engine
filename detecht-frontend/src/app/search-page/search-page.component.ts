import {Component, OnInit, Input, ViewChild} from '@angular/core';
import {environment} from '../../environments/environment';
import {SearchResponse} from '../data-types';
import {SearchService} from '../network-services/search.service';
import {SearchResultPreviewComponent} from './search-result-preview/search-result-preview.component';


@Component({
  selector: 'app-search-page',
  templateUrl: './search-page.component.html',
  styleUrls: ['./search-page.component.scss']
})
export class SearchPageComponent implements OnInit {
  staticUrl: string;
  @Input() result: SearchResponse;

  constructor(
    private searchService: SearchService,
  ) {
  }


  ngOnInit() {
    this.staticUrl = environment.staticUrl;
  }

}
