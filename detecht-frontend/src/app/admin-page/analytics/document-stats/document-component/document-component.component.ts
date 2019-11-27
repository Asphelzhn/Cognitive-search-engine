import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-document-component',
  templateUrl: './document-component.component.html',
  styleUrls: ['./document-component.component.scss']
})
export class DocumentComponentComponent implements OnInit {
  @Input() title: string;
  @Input() abstract: string;
  icon: string;
  constructor() { }

  ngOnInit() {
    let index = Math.round(Math.random() * 2 + 1);
    this.icon = '../../../../../assets/admin-page/color-bar-' + index + '-icon.png';

  }

}
