import {Component, Input, OnInit, ViewChild} from '@angular/core';
import {SearchResponse} from '../../data-types';
import {PreviewMessageService} from '../../message-services/preview-message.service';
import {PdfViewerComponent} from 'ng2-pdf-viewer';

@Component({
  selector: 'app-search-result-preview',
  templateUrl: './search-result-preview.component.html',
  styleUrls: ['./search-result-preview.component.scss']
})

export class SearchResultPreviewComponent implements OnInit {

  constructor(
    private previewData: PreviewMessageService
  ) {
  }

  @Input() showPreview: boolean;
  @Input() showAllPages: boolean;
  @Input() staticUrl: string;
  @Input() result: SearchResponse;
  @Input() sentence: string;
  @Input() page: number;
  @ViewChild(PdfViewerComponent, {static: false}) private pdfViewer;

  closeMessage() {
    this.previewData.changeMessage(false);
  }

  search() {
    if (this.sentence !== undefined) {
      this.pdfViewer.pdfFindController.executeCommand('find', {
        caseSensitive: false, findPrevious: undefined, highlightAll: true, phraseSearch: true, query: this.sentence
      });
    }
  }

  ngOnInit() {
  }
}
