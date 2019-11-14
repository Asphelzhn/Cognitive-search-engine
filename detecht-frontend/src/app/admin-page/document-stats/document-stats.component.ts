import { Component, OnInit, Pipe, PipeTransform } from '@angular/core';
import {Pdf} from '../../data-types';
import {AdminService} from '../../network-services/admin.service';

@Component({
  selector: 'app-document-stats',
  templateUrl: './document-stats.component.html',
  styleUrls: ['./document-stats.component.scss']
})
export class DocumentStatsComponent implements OnInit {

    showDownloads: boolean;
    pdfs: Pdf[];
    id: number;
  constructor(private adminService: AdminService) { }

  sortFavoritesArray() {
    console.log('favorites: ' + this.pdfs);
    this.pdfs.sort((a, b) => b.favorites - a.favorites);

  }

  sortDownloadsArray() {
    console.log('in downloads');
    this.pdfs.sort((a, b) => b.downloads - a.downloads);
  }

  ngOnInit() {
    this.showDownloads = false;
    this.pdfs = [];
    this.adminService.getAllPdf().subscribe(
      (data: any) => {
        data.data = data;
        for (const pdf of data.data) {
      //    console.log(pdf.id, pdf.file.split('/static/pdf/')[1]);
          // this.pdfs.push( new Pdf(pdf.id, pdf.file.split('/static/pdf/')[1], pdf.title, pdf.downloads, pdf.favorites));
          this.pdfs.push( new Pdf(pdf.id, pdf.file.split('/static/pdf/')[1], pdf.title,
            Math.floor(Math.random() * Math.floor(100)), Math.floor(Math.random() * Math.floor(100))));
        }
        this.sortFavoritesArray();
      },
      (error: any) => {
        console.log(error);
      }
    );
  }
}
