import {Component, OnInit, Input, EventEmitter, Output} from '@angular/core';
import {SearchResponse} from '../../../data-types';
import {environment} from '../../../../environments/environment';
import {MatDialog, MatDialogConfig} from '@angular/material';
import {SearchHitPreviewComponent} from '../../search-hit-preview/search-hit-preview.component';
import {PreviewMessageService} from '../../../message-services/preview-message.service';
import {FileSaverModule} from 'ngx-filesaver';
import {SearchHitPreviewService} from '../../../message-services/search-hit-preview.service';


@Component({
  selector: 'app-result-bar',
  templateUrl: './result-bar.component.html',
  styleUrls: ['./result-bar.component.scss']
})
export class ResultBarComponent implements OnInit {

  staticUrl: string;
  showPreview: boolean;
  showSentences: boolean;
  liked: boolean;
  @Output() removeEvent: EventEmitter<string> = new EventEmitter();
  @Input() result: SearchResponse;

  constructor(
    private previewData: PreviewMessageService,
    private searchHitPreviewService: SearchHitPreviewService
  ) {
  }

  removeResult(remove: string) {
    this.removeEvent.emit(remove);
  }

  openDialog() {
    this.searchHitPreviewService.changeResult(this.result);
  }

  ngOnInit() {
    this.staticUrl = environment.staticUrl;
    this.showSentences = false;
    this.previewData.currentMessage.subscribe(showPreview => this.showPreview = showPreview);

    // Ändras sen, behöver API
    this.liked = false;

  }
}
