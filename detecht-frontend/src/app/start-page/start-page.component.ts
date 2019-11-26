import { Component, OnInit } from '@angular/core';
import {InteractWithDocumentService} from '../network-services/interact-with-document.service';
import {PreviewMessageService} from "../message-services/preview-message.service";
import {NetworkInteractWithDocumentRequest} from '../network-services/network-data-types';

@Component({
  selector: 'app-start-page',
  templateUrl: './start-page.component.html',
  styleUrls: ['./start-page.component.scss']
})
export class StartPageComponent implements OnInit {

  constructor(private interact: InteractWithDocumentService) { }
  test: NetworkInteractWithDocumentRequest;

  ngOnInit() {
    this.test =  new NetworkInteractWithDocumentRequest()
    // test: NetworkInteractWithDocumentRequest;
    this.test.pdfName = 'apa';
    this.test.userId = 'hej';
    this.interact.previewDocument(this.test);
  }

}
