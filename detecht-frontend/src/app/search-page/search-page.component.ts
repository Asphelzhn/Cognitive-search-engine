import {Component, OnInit, Input, ViewChild} from '@angular/core';
import {environment} from '../../environments/environment';
import {SearchResponse} from '../data-types';
import {SearchHitPreviewService} from '../message-services/search-hit-preview.service';

@Component({
  selector: 'app-search-page',
  templateUrl: './search-page.component.html',
  styleUrls: ['./search-page.component.scss']
})
export class SearchPageComponent implements OnInit {
  staticUrl: string;
  @Input() result: SearchResponse;
  previewResult: SearchResponse;

  constructor(private searchHitPreviewService: SearchHitPreviewService) {
  }

  ngOnInit() {
    this.staticUrl = environment.staticUrl;
    this.searchHitPreviewService.result.subscribe(result => this.previewResult = result);
  }

}
