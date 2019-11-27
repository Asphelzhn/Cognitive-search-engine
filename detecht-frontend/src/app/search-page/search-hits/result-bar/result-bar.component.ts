import {Component, OnInit, Input, EventEmitter, Output} from '@angular/core';
import {SearchResponse} from '../../../data-types';
import {environment} from '../../../../environments/environment';
import {MatDialog, MatDialogConfig} from '@angular/material';
import {SearchHitPreviewComponent} from '../../search-hit-preview/search-hit-preview.component';
import {PreviewMessageService} from '../../../message-services/preview-message.service';
import {FileSaverModule} from 'ngx-filesaver';
import {SearchHitPreviewService} from '../../../message-services/search-hit-preview.service';
import {NetworkFavoriteDocumentRequest, NetworkInteractWithDocumentRequest} from '../../../network-services/network-data-types';
import {InteractWithDocumentService} from '../../../network-services/interact-with-document.service';
import {UserFavoriteService} from '../../../network-services/user-favorite.service';


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
  userId: number;
  @Output() removeEvent: EventEmitter<string> = new EventEmitter();
  @Input() result: SearchResponse;

  constructor(
    private previewData: PreviewMessageService,
    private searchHitPreviewService: SearchHitPreviewService,
    private interactWithDocumentService: InteractWithDocumentService,
    private userFavoriteService: UserFavoriteService
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

    this.userId = 0;

  }

  downloadInteraction(): void {
    const data = new NetworkInteractWithDocumentRequest(this.result.name, 0, 'Download');
    this.interactWithDocumentService.downloadDocument(data);
  }

  like(pdfName: string, like: boolean): void {
    const data = new NetworkFavoriteDocumentRequest();
    data.pdfName = pdfName;
    data.userId = this.userId;
    data.like = like;
    this.userFavoriteService.favoriteDocument(data);
  }

}
