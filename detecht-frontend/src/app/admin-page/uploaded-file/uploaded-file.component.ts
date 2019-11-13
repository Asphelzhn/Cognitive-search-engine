import {Component, OnInit} from '@angular/core';
import {AdminService} from '../../network-services/admin.service';
import {NetworkGetAllPdfResponse, NetworkPdfUploadResponse} from '../../network-services/network-data-types';
import {Pdf} from '../../data-types';

@Component({
  selector: 'app-uploaded-file',
  templateUrl: './uploaded-file.component.html',
  styleUrls: ['./uploaded-file.component.scss']
})
export class UploadedFileComponent implements OnInit {

  pdfs: Pdf[];

  constructor(private adminService: AdminService) { }

  ngOnInit() {
    this.pdfs = [];
    this.adminService.getAllPdf().subscribe(
      (data: any) => {
        console.log(data);
        data.data = data;
        for (const pdf of data.data) {
          console.log(pdf.id, pdf.file.split('/static/pdf/')[1]);
          // this.pdfs.push( new Pdf(pdf.id, pdf.file.split('/static/pdf/')[1], pdf.title, pdf.downloads, pdf.favorites));
          this.pdfs.push( new Pdf(pdf.id, pdf.file.split('/static/pdf/')[1], pdf.title,
            Math.floor(Math.random() * Math.floor(100)), Math.floor(Math.random() * Math.floor(100))));
        }
        console.log(this.pdfs);
      },
      (error: any) => {
        console.log(error);
      }
    );
  }

  deletePDF(fileName: string): void {
    console.log('Delete ' + fileName);
  }
}
