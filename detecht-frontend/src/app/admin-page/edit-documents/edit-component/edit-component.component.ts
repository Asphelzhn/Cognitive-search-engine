import { Component, Input, OnInit } from '@angular/core';
import {ChangeNameService} from '../../../network-services/change-name.service';
import {NetworkChangeNameRequest} from '../../../network-services/network-data-types';
import {Router} from '@angular/router';

@Component({
  selector: 'app-edit-component',
  templateUrl: './edit-component.component.html',
  styleUrls: ['./edit-component.component.scss']
})
export class EditComponentComponent implements OnInit {

  @Input() pdfName: string;
  changeToName: string;
  data: NetworkChangeNameRequest;

  constructor(private changeNameService: ChangeNameService, private router: Router) { }

  ngOnInit() {
  }

  changeName() {
    if (this.changeToName !== '') {
      this.data.newName = this.changeToName;
      this.data.oldName = this.pdfName;
      this.changeNameService.changeName(this.data);
      this.pdfName = this.changeToName;
    }
  }

}
