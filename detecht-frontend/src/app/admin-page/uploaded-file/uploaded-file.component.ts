import {Component, OnInit} from '@angular/core';
import {AdminService} from '../../network-services/admin.service';
import {Pdf, SearchResponse} from '../../data-types';
import {SearchService} from '../../network-services/search.service';

@Component({
  selector: 'app-uploaded-file',
  templateUrl: './uploaded-file.component.html',
  styleUrls: ['./uploaded-file.component.scss']
})
export class UploadedFileComponent implements OnInit {

  pdfs: Pdf[];
  searchString: string;
  searched: boolean;
  results: SearchResponse[];

  constructor(private adminService: AdminService,
              private searchService: SearchService
  ) {
  }

  search(): void {
    console.log('Searching for: ' + this.searchString);
    this.searchService.search(this.searchString);
    this.searched = true;
  }

 // deletePDF(fileName: string): void {
  //  console.log('Delete ' + fileName);
 // }

  ngOnInit() {
    this.pdfs = [];
    this.searched = false;
    this.adminService.getAllPdf().subscribe(
      (data: any) => {
        console.log(data);
        data.data = data;
        for (const pdf of data.data) {
          console.log(pdf.id, pdf.file.split('/static/pdf/')[1]);
          // this.pdfs.push( new Pdf(pdf.id, pdf.file.split('/static/pdf/')[1], pdf.title, pdf.downloads, pdf.favorites));
          this.pdfs.push(new Pdf(pdf.id, pdf.file.split('/static/pdf/')[1], pdf.title,
            Math.floor(Math.random() * Math.floor(100)), Math.floor(Math.random() * Math.floor(100))));
        }
        console.log(this.pdfs);
      },
      (error: any) => {
        console.log(error);
      }
    );

    this.searchService.searchResponse.subscribe(searchResult => this.results = searchResult);
  }
}
