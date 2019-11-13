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
    pdfFavorites: Pdf[];
    pdfDownloads: Pdf[];
    id: number;
    pdfTest: [{id}, {id}, {id}, {id}, {id}, {id}, {id}];
  constructor(private adminService: AdminService) { }

  sortFavoritesArray() {
    this.pdfTest = [{id: 7}, {id: 5}, {id: 35}, {id: 4}, {id: 35}, {id: 100}, {id: 1}];
    console.log('in favorites' + this.pdfs[0].favorites);
    this.pdfFavorites = this.pdfs;
    this.pdfFavorites.sort((a, b) => a.favorites - b.favorites);
    console.log(this.pdfFavorites);
    this.pdfTest.sort((a, b) => a.id - b.id);

  }

  sortDownloadsArray() {
    console.log('in downloads');
    this.pdfDownloads = this.pdfs;
    this.pdfDownloads.sort((a, b) => a.downloads - b.downloads);
  }

  ngOnInit() {
    this.showDownloads = false;
    this.pdfs = [];
    this.pdfTest = [{id: 0}, {id: 0}, {id: 0}, {id: 0}, {id: 0}, {id: 0}, {id: 0}];
    this.adminService.getAllPdf().subscribe(
      (data: any) => {
    //    console.log(data);
        data.data = data;
        for (const pdf of data.data) {
      //    console.log(pdf.id, pdf.file.split('/static/pdf/')[1]);
          // this.pdfs.push( new Pdf(pdf.id, pdf.file.split('/static/pdf/')[1], pdf.title, pdf.downloads, pdf.favorites));
          this.pdfs.push( new Pdf(pdf.id, pdf.file.split('/static/pdf/')[1], pdf.title,
            Math.floor(Math.random() * Math.floor(100)), Math.floor(Math.random() * Math.floor(100))));
        }
      //  console.log(this.pdfs);
      },
      (error: any) => {
        console.log(error);
      }
    );
  }
}
