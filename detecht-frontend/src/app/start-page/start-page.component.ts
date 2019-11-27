import { Component, OnInit } from '@angular/core';
import {AdminLoginService} from '../network-services/admin-login.service';
import {PreviewMessageService} from "../message-services/preview-message.service";
import {NetworkAdminLoginRequest} from '../network-services/network-data-types';

@Component({
  selector: 'app-start-page',
  templateUrl: './start-page.component.html',
  styleUrls: ['./start-page.component.scss']
})
export class StartPageComponent implements OnInit {

  constructor(private interact: AdminLoginService) { }
  test: NetworkAdminLoginRequest;

  ngOnInit() {
    this.test =  new NetworkAdminLoginRequest()
    // test: NetworkInteractWithDocumentRequest;
    this.test.username = 'apa';
    this.test.password = 'bananbanan';
    //this.test.userId = 2;
    this.interact.adminLogin(this.test).subscribe(
      response => console.log(response)
    );
  }

}
