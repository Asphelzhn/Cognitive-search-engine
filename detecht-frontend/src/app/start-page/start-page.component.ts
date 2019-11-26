import { Component, OnInit } from '@angular/core';
import {UserFavoriteService} from '../network-services/user-favorite.service';
import {PreviewMessageService} from "../message-services/preview-message.service";
import {NetworkFavoriteDocumentRequest} from '../network-services/network-data-types';

@Component({
  selector: 'app-start-page',
  templateUrl: './start-page.component.html',
  styleUrls: ['./start-page.component.scss']
})
export class StartPageComponent implements OnInit {

  constructor(private interact: UserFavoriteService) { }
  test: NetworkFavoriteDocumentRequest;

  ngOnInit() {
    this.test =  new NetworkFavoriteDocumentRequest()
    // test: NetworkInteractWithDocumentRequest;
    this.test.pdfName = 'apa';
    this.test.userId = 2;
    this.interact.favoriteDocument(this.test);
  }

}
