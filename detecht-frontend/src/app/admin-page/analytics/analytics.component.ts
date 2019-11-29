import {Component, OnInit} from '@angular/core';
import {AdminService} from '../../network-services/admin.service';
import {Pdf, SearchResponse} from '../../data-types';
import {GetAnalyticsService} from '../../network-services/get-analytics.service';
import {NetworkGetAnalyticsResponse} from '../../network-services/network-data-types';

@Component({
  selector: 'app-analytics',
  templateUrl: './analytics.component.html',
  styleUrls: ['./analytics.component.scss']
})
export class AnalyticsComponent implements OnInit {

  pdfs: Pdf[];
  results: Pdf[];
  searchString: string;

  numberDownloads: number;
  numberFavorites: number;
  numberDocuments: number;

  constructor(private adminService: AdminService, private getAnalyticsService: GetAnalyticsService) {
  }

  search(): void {
    console.log('Searching for: ' + this.searchString);
    this.results = [];
    for (const pdf of this.pdfs) {
      console.log(pdf);
      if (pdf.title.toLowerCase().includes(this.searchString.toLowerCase())) {
        this.results.push(pdf);
      }
    }
    console.log('Result');
    console.log(this.results);
  }

 // deletePDF(fileName: string): void {
  //  console.log('Delete ' + fileName);
 // }

  ngOnInit() {
    this.searchString = '';
    this.pdfs = [];
    this.adminService.getAllPdf().subscribe(
      (data: any) => {
        console.log(data);
        data.data = data;
        for (const pdf of data.data) {
          console.log(pdf.id, pdf.file.split('/static/pdf/')[1]);
          this.pdfs.push( new Pdf(pdf.id, pdf.file.split('/static/pdf/')[1], pdf.title, pdf.downloads, pdf.favorites));
        }
        console.log(this.pdfs);
        this.results = this.pdfs;
      },
      (error: any) => {
        console.log(error);
      }
    );

    this.getAnalyticsService.getAnalytics().subscribe(
      (data: NetworkGetAnalyticsResponse) => {
        this.numberDocuments = data.documents;
        this.numberDownloads = data.downloads;
        this.numberFavorites = data.favorites;
      },
      (error: any) => {
        console.log(error);
      }
    );

  }
}
