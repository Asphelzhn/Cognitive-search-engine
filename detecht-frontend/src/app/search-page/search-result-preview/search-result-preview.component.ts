import {Component, Input, OnInit} from '@angular/core';
import {SearchResponse} from '../../data-types';

@Component({
  selector: 'app-search-result-preview',
  templateUrl: './search-result-preview.component.html',
  styleUrls: ['./search-result-preview.component.scss']
})
export class SearchResultPreviewComponent implements OnInit {

  constructor() { }

  @Input() showPreview: boolean;
  @Input() staticUrl: string;
  @Input() result: SearchResponse;


  ngOnInit() {
  }

}
