import { Component, OnInit } from '@angular/core';
import {AdminService} from '../../network-services/admin.service';

@Component({
  selector: 'app-upload-file',
  templateUrl: './upload-file.component.html',
  styleUrls: ['./upload-file.component.scss']
})
export class UploadFileComponent implements OnInit {

  constructor(private adminService: AdminService) {
  }

  fileData: {title: string, file: File}[];
  previewUrl: any = null;
  fileUploadProgress: string = null;
  uploadedFilePath: string = null;
  responseMessage: string;
  uploadingPopUp: boolean;
  doneUploading: boolean;

  ngOnInit() {
    this.fileData = [];
    this.adminService.responseMessage.subscribe(responseMessage => this.responseMessage = responseMessage);
    this.uploadingPopUp = false;
  }

  fileProgress(fileInput: any) {
    for (const file of fileInput.target.files) {
      this.fileData.push({file: file as File, title: this.generateTitle(file.name)});
    }
  }

  generateTitle(pdfname: string): string {
    // Write function for generate title from pdfname. If backend does it.
    let title = pdfname;

    title = title.replace(/_/g, ' ').replace('.pdf', '');
    title = title[0].toLocaleUpperCase() + title.slice(1).toLocaleLowerCase()
    return title;
  }

  onSubmit() {

    this.adminService.pdfUpload(this.fileData);
    this.uploadingPopUp = true;
  }

  closePopup() {
  this.uploadingPopUp = false;
  }
}


