import {Component, OnInit, Input, EventEmitter, Output} from '@angular/core';
import {Abstract, SearchResponse} from '../../../data-types';
import {environment} from '../../../../environments/environment';
import {MatDialog, MatDialogConfig} from '@angular/material';
import {SearchHitPreviewComponent} from '../../search-hit-preview/search-hit-preview.component';
import {PreviewMessageService} from '../../../message-services/preview-message.service';
import {FileSaverModule} from 'ngx-filesaver';
import {SearchHitPreviewService} from '../../../message-services/search-hit-preview.service';
import {
  NetworkAbstractRequest, NetworkAbstractResponse,
  NetworkFavoriteDocumentRequest,
  NetworkInteractWithDocumentRequest
} from '../../../network-services/network-data-types';
import {InteractWithDocumentService} from '../../../network-services/interact-with-document.service';
import {UserFavoriteService} from '../../../network-services/user-favorite.service';
import {SearchService} from '../../../network-services/search.service';
import {AdminLoginService} from '../../../network-services/admin-login.service';


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
  abstracts: Abstract[];
  query: string;
  @Output() removeEvent: EventEmitter<string> = new EventEmitter();
  @Input() result: SearchResponse;

  constructor(
    private searchService: SearchService,
    private previewData: PreviewMessageService,
    private searchHitPreviewService: SearchHitPreviewService,
    private interactWithDocumentService: InteractWithDocumentService,
    private adminLoginService: AdminLoginService,
    private userFavoriteService: UserFavoriteService
  ) {
  }

  removeResult(remove: string) {
    this.removeEvent.emit(remove);
  }

  openDialog() {
    this.searchHitPreviewService.changeResult(this.result, this.abstracts);
  }

  ngOnInit() {
    this.staticUrl = environment.staticUrl;
    this.showSentences = false;
    this.previewData.currentMessage.subscribe(showPreview => this.showPreview = showPreview);

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
    });

    this.searchService.currentSearch.subscribe(query => this.query = query);
    this.searchService.abstract(new NetworkAbstractRequest(this.query, this.result.name)).subscribe(
      (data: NetworkAbstractResponse) => {
        if (data.success) {
          this.abstracts = [];
          for (const abstract of data.abstracts) {
            this.abstracts.push(new Abstract(abstract.sentence, abstract.score, abstract.page));
          }
        } else {
          console.log('Error when getting schedule, please refresh the results');
        }
      },
      (error: any) => {
        console.log(error);
      }
    );

  }

  downloadInteraction(): void {
    const data = new NetworkInteractWithDocumentRequest(this.result.name, this.userId, 'Download');
    this.interactWithDocumentService.downloadDocument(data);
  }

  like(pdfName: string, like: boolean): void {
    this.userFavoriteService.favoriteDocument(new NetworkFavoriteDocumentRequest(this.userId, pdfName, like));
  }

  topAbstract(): Abstract {
    let bestScore = new Abstract('', -1000, 0);
    for (const abstract of this.abstracts) {
      if (abstract.score > bestScore.score) {
        bestScore = abstract;
      }
    }
    return bestScore;
  }

}
