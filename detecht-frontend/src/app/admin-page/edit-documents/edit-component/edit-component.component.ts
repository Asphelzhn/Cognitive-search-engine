import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-edit-component',
  templateUrl: './edit-component.component.html',
  styleUrls: ['./edit-component.component.scss']
})
export class EditComponentComponent implements OnInit {

  @Input() pdfName: string;

  constructor() { }

  ngOnInit() {
  }

}
