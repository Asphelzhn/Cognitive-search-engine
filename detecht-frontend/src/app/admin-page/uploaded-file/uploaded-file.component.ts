import {Component, OnInit} from '@angular/core';
import {AdminService} from '../../network-services/admin.service';

@Component({
  selector: 'app-uploaded-file',
  templateUrl: './uploaded-file.component.html',
  styleUrls: ['./uploaded-file.component.scss']
})
export class UploadedFileComponent implements OnInit {

  // pdfs: any[];

  constructor(private adminService: AdminService) { }

  ngOnInit() {
    // this.adminService.getAllPdf().subscribe(pdfs => this.pdfs = pdfs);
  }

  deletePDF(fileName: string): void {
    console.log('Delete ' + fileName);
  }
}
