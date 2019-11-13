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
  constructor(private adminService: AdminService) { }

  sortFavoritesArray() {
    console.log('in favorites' + this.pdfs);
    this.pdfs.sort((a, b) => a.favorites - b.favorites);
    this.pdfFavorites = this.pdfs;
    console.log('pdf favorites: ' + this.pdfFavorites);
    console.log('after pdf favorites');
  }

  sortDownloadsArray() {
   this.pdfDownloads = this.pdfs.sort((a, b) => a.downloads - b.downloads);
  }

  ngOnInit() {
    this.showDownloads = true;
    this.pdfs = [];
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
