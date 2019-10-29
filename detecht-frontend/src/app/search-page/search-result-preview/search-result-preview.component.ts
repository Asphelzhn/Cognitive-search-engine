import {Component, Input, OnInit} from '@angular/core';
import {SearchResponse} from '../../data-types';
import {PreviewMessageService} from '../../message-services/preview-message.service';

@Component({
  selector: 'app-search-result-preview',
  templateUrl: './search-result-preview.component.html',
  styleUrls: ['./search-result-preview.component.scss']
})
export class SearchResultPreviewComponent implements OnInit {

  constructor(
    private data: PreviewMessageService
  ) {
  }

  @Input() showPreview: boolean;
  @Input() staticUrl: string;
  @Input() result: SearchResponse;

  closeMessage() {
    this.data.changeMessage(false);
  }

  ngOnInit() {
    this.showPreview = false;
  }

}
