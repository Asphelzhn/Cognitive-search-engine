import {Component, Inject, Input, OnInit} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from '@angular/material';
import {environment} from '../../../environments/environment';
import {Abstract, SearchResponse} from '../../data-types';
import {SearchService} from '../../network-services/search.service';
import {PreviewMessageService} from '../../message-services/preview-message.service';
import {
  NetworkFavoriteDocumentRequest,
  NetworkInteractWithDocumentRequest, NetworkRelatedDocumentResponse
} from '../../network-services/network-data-types';
import {SearchHitPreviewService} from '../../message-services/search-hit-preview.service';
import {InteractWithDocumentService} from '../../network-services/interact-with-document.service';
import {RelatedDocumentService} from '../../network-services/related-document.service';
import {UserFavoriteService} from '../../network-services/user-favorite.service';
import {AdminLoginService} from '../../network-services/admin-login.service';

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
  rightPage: number;
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
    private adminLoginService: AdminLoginService,
    private searchService: SearchService,
    private userFavoriteService: UserFavoriteService
  ) { }

  close() {
    this.searchHitPreviewService.changeResult(undefined, []);
  }

  ngOnInit() {

    this.searchService.currentSearch.subscribe(query => this.query = query);

    this.staticUrl = environment.staticUrl;
    this.previewData.currentMessage.subscribe(showPreview => this.showPreview = showPreview);

    this.pdfUrl = environment.pdfUrl;

    this.adminLoginService.userId.subscribe((userId) => {
      this.userId = userId;
      this.userFavoriteService.isFavorite(new NetworkFavoriteDocumentRequest(userId, this.result.name, true)).subscribe(
        (data) => {
          if (data.success) {
            this.liked = data.favorite;
          } else {
            console.log('Error looking if doc is favorite');
          }
        },
        (error) => {
          console.log(error);
        }
      );

      this.relatedDocumentService.relatedDocument({pdfName: this.result.name, userId: userId}).subscribe(
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

    });

  }

  displayPreview(abstract: Abstract): void {
    this.showPreview = true;
    this.rightSentence = abstract.sentence;
    this.rightPage = abstract.page;
    const data = new NetworkInteractWithDocumentRequest(this.result.name, this.userId, 'Preview');
    this.interactWithDocumentService.previewDocument(data);
  }

  downloadInteraction(): void {
    const data = new NetworkInteractWithDocumentRequest(this.result.name, this.userId, 'Download');
    this.interactWithDocumentService.downloadDocument(data);
  }

  like(pdfName: string, like: boolean): void {
    this.userFavoriteService.favoriteDocument(new NetworkFavoriteDocumentRequest(this.userId, pdfName, like));
  }

  changeDocument(pdfName: string): void {
    this.searchService.getDoc(pdfName, this.query).subscribe(
      (data) => {
        if (data.success) {
          const newAbstracts = [];
          for (const abstract of data.abstracts) {
            newAbstracts.push(new Abstract(abstract.sentence, abstract.score, abstract.page));
          }
          this.searchHitPreviewService.changeResult(new SearchResponse(data.pdfTitle, data.pdfName, data.keywords), newAbstracts);
        }
      },
      (error) => {
        console.log(error);
      }
    );
  }

}
