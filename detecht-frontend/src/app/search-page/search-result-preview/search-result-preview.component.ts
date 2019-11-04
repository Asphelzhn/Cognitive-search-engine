import {Component, Input, OnInit, ViewChild } from '@angular/core';
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
  searchString: string;
  @Input() staticUrl: string;
  @Input() result: SearchResponse;
  @ViewChild(PdfViewerComponent, {static: false}) private pdfViewer;

  closeMessage() {
    this.previewData.changeMessage(false);
  }

  search(searchString) {
    console.log(this.searchString);
    this.pdfViewer.pdfFindController.executeCommand('find', {
      caseSensitive: false, findPrevious: undefined, highlightAll: true, phraseSearch: true, query: searchString
    });
    console.log('after search');
  }

  firstFunction(searchString: string) {
    this.searchString = searchString;
    alert(this.searchString);
  }

  ngOnInit() {
    if (this.previewData.subsVar === undefined) {
        this.previewData.subsVar = this.previewData.invokeSearch.subscribe((searchString: string) => {
          this.firstFunction(searchString);
        });
      }
  }
}
