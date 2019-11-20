import { Component, OnInit } from '@angular/core';
import {AdminService} from '../../network-services/admin.service';
import {NetworkPdfUploadRequest} from '../../network-services/network-data-types';

@Component({
  selector: 'app-upload-file',
  templateUrl: './upload-file.component.html',
  styleUrls: ['./upload-file.component.scss']
})
export class UploadFileComponent implements OnInit {

  constructor(private adminService: AdminService) { }

  fileTitles: string[];
  fileData: File[];
  previewUrl: any = null;
  fileUploadProgress: string = null;
  uploadedFilePath: string = null;
  responseMessage: string;

  ngOnInit() {
    this.fileTitles = [];
    this.fileData = [];
    this.adminService.responseMessage.subscribe(responseMessage => this.responseMessage = responseMessage);
  }

  fileProgress(fileInput: any) {
    for (const file of fileInput.target.files) {
      this.fileData.push(file as File);
      this.fileTitles.push(this.generateTitle(file.name));
    }
    this.preview();
  }

  generateTitle(pdfname: string): string {
    return pdfname;
  }

  preview() {
    // Show preview TODO
    // const mimeType = this.fileData.type;
    // if (mimeType.match(/image\/*/) == null) {
    //   return;
    // }

    // const reader = new FileReader();
    // // TODO
    // // reader.readAsDataURL(this.fileData);
    // reader.onload = (event) => {
    //   this.previewUrl = reader.result;
    // };
  }


  onSubmit() {
    // const networkPdfUploadRequest = new NetworkPdfUploadRequest(this.fileTitle, this.fileData);
    // this.adminService.pdfUpload(networkPdfUploadRequest);
    // TODO ta med oven
    // const formData = new FormData();
    // formData.append('file', this.fileData);
    // console.log('Submitting');
    // this.http.post('url/to/your/api', formData)
    //   .subscribe(res => {
    //     console.log(res);
    //     // this.uploadedFilePath = res.data.filePath;
    //     alert('SUCCESS !!');
    //   });
  }
}
