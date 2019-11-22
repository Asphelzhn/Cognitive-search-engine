import { Component, OnInit } from '@angular/core';
import {AdminService} from '../../network-services/admin.service';
import {NetworkPdfUploadRequest} from '../../network-services/network-data-types';
import {count} from "rxjs/operators";
import {getSortHeaderNotContainedWithinSortError} from "@angular/material/sort/typings/sort-errors";

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
  }
  generateTitle(pdfname: string): string {
    // Write function for generate title from pdfname. If backend does it.
    var title = pdfname;

    for (const i of pdfname[length]) {
      if (pdfname.charAt(Number(i)) == '_') {
        title.charAt(Number(i)) == ' ';
      }
    }

    return title;
  }

  //((preview() {
  //}

  onSubmit() {
    for (const i of this.fileTitles[length]) {
      const networkPdfUploadRequest = new NetworkPdfUploadRequest(this.fileTitles[i], this.fileData[i]);
      this.adminService.pdfUpload(networkPdfUploadRequest);
      console.log(i);
    }
    alert('SUCCESS !!');

    // TODO ta med ovan
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
