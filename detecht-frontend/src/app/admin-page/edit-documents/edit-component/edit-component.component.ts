import { Component, Input, OnInit } from '@angular/core';
import {ChangeNameService} from '../../../network-services/change-name.service';
import {NetworkChangeNameRequest} from "../../../network-services/network-data-types";

@Component({
  selector: 'app-edit-component',
  templateUrl: './edit-component.component.html',
  styleUrls: ['./edit-component.component.scss']
})
export class EditComponentComponent implements OnInit {

  @Input() pdfName: string;
  changeToName: string;
  data: NetworkChangeNameRequest;

  constructor(private changeNameService: ChangeNameService) { }

  ngOnInit() {
  }

  changeName() {
    if (this.changeToName !== ''){
      this.data.newName = this.changeToName;
      this.data.newName = this.pdfName;
      this.changeNameService.changeName(this.data);
    }
  }

}
