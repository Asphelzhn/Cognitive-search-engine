import {Component, Input, OnInit} from '@angular/core';
import {NetworkFavoriteDocumentRequest, NetworkInteractWithDocumentRequest} from '../../network-services/network-data-types';
import {InteractWithDocumentService} from '../../network-services/interact-with-document.service';
import {UserFavoriteService} from '../../network-services/user-favorite.service';

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
  userId: number;


  constructor(private interactWithDocumentService: InteractWithDocumentService, private userFavoriteService: UserFavoriteService) {}



  ngOnInit() {
    this.sentence1 = this.boldstring(this.inputsentence1, this.keyword);
    this.sentence2 = this.boldstring(this.inputsentence2, this.keyword);
    this.sentence3 = this.boldstring(this.inputsentence3, this.keyword);
    this.title = this.boldstring(this.inputtitle, this.keyword);

    this.userId = 0;

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
    const data = new NetworkFavoriteDocumentRequest();
    data.pdfName = this.inputfile;
    data.userId = this.userId;
    data.like = like;
    this.userFavoriteService.favoriteDocument(data);
  }
}
