import { Component, Input, OnInit } from '@angular/core';
import {ChangeNameService} from '../../../network-services/change-name.service';
import {NetworkChangeNameRequest} from '../../../network-services/network-data-types';
import {Router} from '@angular/router';
import {SearchResponse} from '../../../data-types';

@Component({
  selector: 'app-edit-component',
  templateUrl: './edit-component.component.html',
  styleUrls: ['./edit-component.component.scss']
})
export class EditComponentComponent implements OnInit {

  @Input() pdf: SearchResponse;
  changeToName: string;
  data: NetworkChangeNameRequest;

  constructor(private changeNameService: ChangeNameService, private router: Router) { }

  ngOnInit() {
    this.changeToName = this.pdf.title;
  }

  changeName() {
    this.data = new NetworkChangeNameRequest();
    if (this.changeToName !== '') {
      this.data.newTitle = this.changeToName;
      this.data.pdfName = this.pdf.name;
      this.changeNameService.changeName(this.data);
      this.pdf.title = this.changeToName;
    }
  }

}
