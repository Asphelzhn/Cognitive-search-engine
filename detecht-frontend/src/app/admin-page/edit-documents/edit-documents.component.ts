import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-edit-documents',
  templateUrl: './edit-documents.component.html',
  styleUrls: ['./edit-documents.component.scss']
})
export class EditDocumentsComponent implements OnInit {

  pdfName:string;
  constructor() { }

  ngOnInit() {
  }

  editDocument($event) {
    this.pdfName = $event;
  }
}
