import {Component, Input, OnInit, Pipe, PipeTransform} from '@angular/core';
import {Pdf} from '../../../data-types';

@Component({
  selector: 'app-document-stats',
  templateUrl: './document-stats.component.html',
  styleUrls: ['./document-stats.component.scss']
})
export class DocumentStatsComponent implements OnInit {

  @Input() pdfs: Pdf[];
  constructor() { }

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

  ngOnInit() {}

}
