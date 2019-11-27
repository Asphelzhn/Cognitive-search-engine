import { Component, OnInit } from '@angular/core';
import {RelatedDocumentService} from '../network-services/related-document.service';
import {PreviewMessageService} from "../message-services/preview-message.service";
import {NetworkRelatedDocumentRequest} from '../network-services/network-data-types';

@Component({
  selector: 'app-start-page',
  templateUrl: './start-page.component.html',
  styleUrls: ['./start-page.component.scss']
})
export class StartPageComponent implements OnInit {

  constructor(private interact: RelatedDocumentService) { }
  test: NetworkRelatedDocumentRequest;

  ngOnInit() {
    this.test =  new NetworkRelatedDocumentRequest()
    // test: NetworkInteractWithDocumentRequest;
    this.test.name = 'apa';
    //this.test.userId = 2;
    this.interact.relatedDocument(this.test);
  }

}
