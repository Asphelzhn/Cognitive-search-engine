import {Component, Inject, Input, OnInit} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from '@angular/material';
import {environment} from '../../../environments/environment';
import {SearchResponse} from '../../data-types';
import {SearchService} from '../../network-services/search.service';
import {PreviewMessageService} from '../../message-services/preview-message.service';
import {
  NetworkAbstractRequest,
  NetworkAbstractResponse, NetworkFavoriteDocumentRequest,
  NetworkInteractWithDocumentRequest, NetworkRelatedDocumentResponse,
  NetworkSearchResponse
} from '../../network-services/network-data-types';
import {SearchHitPreviewService} from '../../message-services/search-hit-preview.service';
import {InteractWithDocumentService} from '../../network-services/interact-with-document.service';
import {RelatedDocumentService} from '../../network-services/related-document.service';
import {UserFavoriteService} from '../../network-services/user-favorite.service';

@Component({
  selector: 'app-search-hit-preview',
  templateUrl: './search-hit-preview.component.html',
  styleUrls: ['./search-hit-preview.component.scss']
})
export class SearchHitPreviewComponent implements OnInit {
  @Input() result: SearchResponse;
  staticUrl: string;
  showPreview: boolean;
  rightSentence: string;
  @Input() abstracts: Abstract[];
  query: string;
  liked: boolean;
  pdfUrl: string;
  userId: number;
  relatedSearches: {
    title: string;
    pdfName: string;
    liked: boolean;
  }[];

  constructor(
    private previewData: PreviewMessageService,
    private searchHitPreviewService: SearchHitPreviewService,
    private interactWithDocumentService: InteractWithDocumentService,
    private relatedDocumentService: RelatedDocumentService,
    private userFavoriteService: UserFavoriteService
  ) { }

  close() {
    this.searchHitPreviewService.changeResult(undefined, []);
  }

  ngOnInit() {

    this.staticUrl = environment.staticUrl;
    this.previewData.currentMessage.subscribe(showPreview => this.showPreview = showPreview);
    this.liked = false;

    this.relatedDocumentService.relatedDocument(this.result.name).subscribe(
      (data: NetworkRelatedDocumentResponse) => {
        if (data.success) {
          this.relatedSearches = [];
          for (const related of data.content) {
            this.relatedSearches.push({title: related.title, pdfName: related.pdfName, liked: related.liked});
          }
          console.log(this.relatedSearches);
        } else {
          console.log('Error when getting schedule, please refresh the results');
        }
      },
      (error: any) => {
        console.log(error);
      }
      );

    this.pdfUrl = environment.pdfUrl;
    this.userId = 0;

  }

  displayPreview(abstract: Abstract): void {
    this.showPreview = true;
    this.rightSentence = abstract.sentence;
    const data = new NetworkInteractWithDocumentRequest(this.result.name, this.userId, 'Preview');
    this.interactWithDocumentService.previewDocument(data);
  }

  downloadInteraction(): void {
    const data = new NetworkInteractWithDocumentRequest(this.result.name, this.userId, 'Download');
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
