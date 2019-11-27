import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-trending-document',
  templateUrl: './trending-document.component.html',
  styleUrls: ['./trending-document.component.scss']
})
export class TrendingDocumentComponent implements OnInit {
  @Input() title: string;
  constructor() { }

  ngOnInit() {
  }

}
