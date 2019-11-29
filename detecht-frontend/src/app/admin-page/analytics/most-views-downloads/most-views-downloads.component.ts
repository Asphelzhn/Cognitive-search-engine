import {Component, Input, OnInit} from '@angular/core';
import {Pdf} from '../../../data-types';

@Component({
  selector: 'app-most-views-downloads',
  templateUrl: './most-views-downloads.component.html',
  styleUrls: ['./most-views-downloads.component.scss']
})
export class MostViewsDownloadsComponent implements OnInit {
  viewscolor: string;
  downloadscolor: string;
  viewactive: boolean;
  @Input() pdfs: Pdf[];
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
    this.sortFavoritesArray();
  }

  changetodownloads() {
    this.viewscolor = '#a0a0a0';
    this.downloadscolor = '#000000';
    this.viewactive = false;
    this.sortDownloadsArray();
  }

  sortFavoritesArray() {
    console.log('in downloads');
    console.log(this.pdfs);
    this.pdfs.sort((a, b) => b.favorites - a.favorites);
  }

  sortDownloadsArray() {
    console.log('in downloads');
    console.log(this.pdfs);
    this.pdfs.sort((a, b) => b.downloads - a.downloads);
  }

}
