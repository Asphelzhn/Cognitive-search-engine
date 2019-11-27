import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-most-views-downloads',
  templateUrl: './most-views-downloads.component.html',
  styleUrls: ['./most-views-downloads.component.scss']
})
export class MostViewsDownloadsComponent implements OnInit {
  viewscolor: string;
  downloadscolor: string;
  viewactive: boolean;
  constructor() { }

  ngOnInit() {
    this.viewscolor = '#000000';
    this.downloadscolor = '#a0a0a0';
    this.viewactive = true;
  }

  changetoview() {
    this.viewscolor = '#000000';
    this.downloadscolor = '#a0a0a0';
    this.viewactive = true;
  }

  changetodownloads() {
    this.viewscolor = '#a0a0a0';
    this.downloadscolor = '#000000';
    this.viewactive = false;
  }
}
