import { Component, OnInit } from '@angular/core';
import {SearchResponse} from '../../data-types';
import {RelatedSearchesService} from '../../network-services/related-searches.service';

@Component({
  selector: 'app-related-search-hits',
  templateUrl: './related-search-hits.component.html',
  styleUrls: ['./related-search-hits.component.scss']
})
export class RelatedSearchHitsComponent implements OnInit {

  sentences: string[];

  constructor(private relatedSearchesService: RelatedSearchesService) { }

  ngOnInit() {
    this.relatedSearchesService.relatedSearches.subscribe(sentences => this.sentences = sentences);
  }


}
