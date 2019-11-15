import { Component, OnInit } from '@angular/core';
import {AdminService} from '../../network-services/admin.service';
import {NetworkPdfUploadRequest} from '../../network-services/network-data-types';

//import {FormBuilder, FormGroup, Validators} from "@angular/forms";
//import {FileUploader} from "ng2-file-upload";
//import {Observable} from "rxjs";
//import {HttpClient} from "@angular/common/http";
//

@Component({
  selector: 'app-upload-file',
  templateUrl: './upload-file.component.html',
  styleUrls: ['./upload-file.component.scss']
})
export class UploadFileComponent implements OnInit {

  constructor(private adminService: AdminService) { }

  fileTitle: string;
  fileData: File = null;
  previewUrl: any = null;
  fileUploadProgress: string = null;
  uploadedFilePath: string = null;
  responseMessage: string;

  ngOnInit() {
    this.fileTitle = '';
    this.adminService.responseMessage.subscribe(responseMessage => this.responseMessage = responseMessage);
  }

  fileProgress(fileInput: any) {
    this.fileData = fileInput.target.files[0] as File;
    this.preview();
  }

  preview() {
    // Show preview
    const mimeType = this.fileData.type;
    if (mimeType.match(/image\/*/) == null) {
      return;
    }

    const reader = new FileReader();
    reader.readAsDataURL(this.fileData);
    reader.onload = (event) => {
      this.previewUrl = reader.result;
    };
  }

  onSubmit() {
    const networkPdfUploadRequest = new NetworkPdfUploadRequest(this.fileTitle, this.fileData);
    this.adminService.pdfUpload(networkPdfUploadRequest);
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

//export class FileUploadComponent implements OnInit {

  //uploadForm: FormGroup;

  //public uploader:FileUploader = new FileUploader({
    //isHTML5: true
  //});
  //title: string = 'Angular File Upload';
  //constructor(private fb: FormBuilder, private http: HttpClient ) { }

  //uploadSubmit(){
    //for (let i = 0; i < this.uploader.queue.length; i++) {
      //let fileItem = this.uploader.queue[i]._file;
      //if(fileItem.size > 10000000){
        //alert("Each File should be less than 10 MB of size.");
        //return;
      //}
    //}
    //for (let j = 0; j < this.uploader.queue.length; j++) {
      //let data = new FormData();
      //let fileItem = this.uploader.queue[j]._file;
      //console.log(fileItem.name);
      //data.append('file', fileItem);
      //data.append('fileSeq', 'seq'+j);
      //data.append( 'dataType', this.uploadForm.controls.type.value);
      //this.uploadFile(data).subscribe(data => alert(data.message));
    //}
    //this.uploader.clearQueue();
  //}

  //uploadFile(data: FormData): Observable {
    //return this.http.post('http://localhost:8080/upload', data);
  //}

  //ngOnInit() {
    //this.uploadForm = this.fb.group({
      //document: [null, null],
      //type:  [null, Validators.compose([Validators.required])]
    //});
  //}
//}
