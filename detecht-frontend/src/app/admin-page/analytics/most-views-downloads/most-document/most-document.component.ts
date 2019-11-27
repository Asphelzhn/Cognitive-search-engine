import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-most-document',
  templateUrl: './most-document.component.html',
  styleUrls: ['./most-document.component.scss']
})
export class MostDocumentComponent implements OnInit {
  @Input() title: string;
  @Input() abstract: string;
  icon: string;
  @Input() views: number;
  @Input() downloads: number;

  constructor() { }

  ngOnInit() {
    let index = Math.round(Math.random() * 2 + 1);
    this.icon = '../../../../../assets/admin-page/color-bar-'+ index + '-icon.png';
  }

}
