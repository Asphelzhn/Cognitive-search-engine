import {Component, Input, OnInit} from '@angular/core';
import {NetworkFavoriteDocumentRequest, NetworkInteractWithDocumentRequest} from '../../network-services/network-data-types';
import {environment} from '../../../environments/environment';
import {InteractWithDocumentService} from '../../network-services/interact-with-document.service';
import {UserFavoriteService} from '../../network-services/user-favorite.service';
import {Abstract, SearchResponse} from '../../data-types';
import {SearchService} from '../../network-services/search.service';
import {SearchHitPreviewService} from '../../message-services/search-hit-preview.service';

@Component({
  selector: 'app-saved-document',
  templateUrl: './saved-document.component.html',
  styleUrls: ['./saved-document.component.scss']
})
export class SavedDocumentComponent implements OnInit {
  @Input() inputtitle: string;
  @Input() inputfile: string;
  @Input() inputsentence1: string;
  @Input() inputsentence2: string;
  @Input() inputsentence3: string;
  @Input() keyword: string;
  sentence1: string;
  sentence2: string;
  sentence3: string;
  title: string;
  @Input() userId: number;
  liked: boolean;
  private staticUrl: string;


  constructor(private interactWithDocumentService: InteractWithDocumentService,
              private userFavoriteService: UserFavoriteService,
              private searchService: SearchService,
              private searchHitPreviewService: SearchHitPreviewService) {}



  ngOnInit() {
    this.staticUrl = environment.staticUrl;
    this.sentence1 = this.boldstring(this.inputsentence1, this.keyword);
    this.sentence2 = this.boldstring(this.inputsentence2, this.keyword);
    this.sentence3 = this.boldstring(this.inputsentence3, this.keyword);
    this.title = this.boldstring(this.inputtitle, this.keyword);

    this.userFavoriteService.isFavorite(new NetworkFavoriteDocumentRequest(this.userId, this.inputfile, true)).subscribe(
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
  }


  boldstring(str, find: string) {
    let re;
    re = new RegExp(find, 'gi');
    return str.replace(re, '<b>' + find.toUpperCase() + '</b>');
  }

  downloadInteraction(): void {
    const data = new NetworkInteractWithDocumentRequest(this.inputfile, this.userId, 'Download');
    this.interactWithDocumentService.downloadDocument(data);
  }

  like(like: boolean): void {
    this.userFavoriteService.favoriteDocument(new NetworkFavoriteDocumentRequest(this.userId, this.inputfile, like));
    location.reload();
  }

  changeDocument(pdfName: string): void {
    this.searchService.getDoc(pdfName, this.keyword).subscribe(
      (data) => {
        console.log(data);
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
