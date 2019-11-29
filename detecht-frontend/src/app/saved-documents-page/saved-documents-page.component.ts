import {Component, OnInit} from '@angular/core';
import {UserFavoriteService} from '../network-services/user-favorite.service';
import {Abstract, SavedDocument, SearchResponse} from '../data-types';
import {NetworkGetFavoriteDocumentsResponse, NetworkRelatedDocumentResponse} from '../network-services/network-data-types';
import {AdminLoginService} from '../network-services/admin-login.service';
import {SearchHitPreviewService} from '../message-services/search-hit-preview.service';

@Component({
  selector: 'app-saved-documents-page',
  templateUrl: './saved-documents-page.component.html',
  styleUrls: ['./saved-documents-page.component.scss']
})
export class SavedDocumentsPageComponent implements OnInit {

  savedDocuments: SavedDocument[] = [];
  userId: number;

  previewResult: SearchResponse;
  abstracts: Abstract[];

  constructor(private userFavoriteService: UserFavoriteService,
              private adminLoginService: AdminLoginService,
              private searchHitPreviewService: SearchHitPreviewService) { }

  ngOnInit() {

    this.searchHitPreviewService.result.subscribe(result => this.previewResult = result);
    this.searchHitPreviewService.abstracts.subscribe(abstracts => this.abstracts = abstracts);

    this.adminLoginService.userId.subscribe((userId) => {
      this.userId = userId;

      console.log(userId);
      this.userFavoriteService.getFavoriteDocuments(userId).subscribe(
        (data: NetworkGetFavoriteDocumentsResponse) => {
          console.log(data);
          if (data.success) {
            this.savedDocuments = [];
            for (const doc of data.pdfs) {
              const abstracts: Abstract[] = [];
              for (const abstract of doc.abstracts) {
                abstracts.push(new Abstract(abstract.sentence, abstract.score, abstract.page));
              }
              this.savedDocuments.push(new SavedDocument(doc.title, doc.pdfName, doc.keywords, abstracts));
            }
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

  getBestKeyword(doc: SavedDocument): string {
    let bestKeyword = '';
    let bestScore = 0;
    for (const keyword of doc.keywords) {
      if (keyword.weight > bestScore) {
        bestScore = keyword.weight;
        bestKeyword = keyword.keyword;
      }
    }
    return bestKeyword;
  }

}
