import {Component, Input, OnInit} from '@angular/core';
import {environment} from '../../../../environments/environment';

@Component({
  selector: 'app-trending-document',
  templateUrl: './trending-document.component.html',
  styleUrls: ['./trending-document.component.scss']
})
export class TrendingDocumentComponent implements OnInit {
  @Input() title: string;
  @Input() pdfName: string;
  staticUrl: string;
  constructor() { }

  ngOnInit() {
    this.staticUrl = environment.staticUrl;
  }

}
