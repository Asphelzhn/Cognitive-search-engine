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
    this.adminService.getAllPdf().subscribe(
      (data: NetworkGetAllPdfResponse) => {
        console.log(data);
        for (const pdf of data.data) {
          let d = 0;
          let f = 3;
          this.pdfs.push( new Pdf(pdf.id, pdf.file, pdf.title, pdf.downloads, pdf.favorites));
          this.pdfs.push( new Pdf(pdf.id, pdf.file, pdf.title, d++, f++));
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
