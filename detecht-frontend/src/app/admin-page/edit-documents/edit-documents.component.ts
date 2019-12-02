import { Component, OnInit } from '@angular/core';
import {SearchResponse} from '../../data-types';

@Component({
  selector: 'app-edit-documents',
  templateUrl: './edit-documents.component.html',
  styleUrls: ['./edit-documents.component.scss']
})
export class EditDocumentsComponent implements OnInit {

  result: SearchResponse;
  constructor() { }

  ngOnInit() {
  }

  editDocument($event) {
    this.result = $event;
  }
}
