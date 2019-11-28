import {Component, OnInit, Input, ViewChild} from '@angular/core';
import {environment} from '../../environments/environment';
import {Abstract, SearchResponse} from '../data-types';
import {SearchHitPreviewService} from '../message-services/search-hit-preview.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-search-page',
  templateUrl: './search-page.component.html',
  styleUrls: ['./search-page.component.scss']
})
export class SearchPageComponent implements OnInit {
  staticUrl: string;
  @Input() result: SearchResponse;
  previewResult: SearchResponse;
  abstracts: Abstract[];

  constructor(private searchHitPreviewService: SearchHitPreviewService,
              private router: Router) {

  }


  ngOnInit() {
    this.staticUrl = environment.staticUrl;
    this.searchHitPreviewService.result.subscribe(result => this.previewResult = result);
    this.searchHitPreviewService.abstracts.subscribe(abstracts => this.abstracts = abstracts);
  }

}
