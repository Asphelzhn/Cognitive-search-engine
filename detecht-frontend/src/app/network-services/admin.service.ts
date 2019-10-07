import { Injectable } from '@angular/core';
import {NetworkService} from './network.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {NetworkPdfUploadResponse, NetworkPdfUploadRequest, NetworkSearchResponse} from './network-data-types';
import {environment} from '../../environments/environment';
import {catchError} from 'rxjs/operators';
import {BehaviorSubject, Observable} from 'rxjs';
import {SearchResponse} from '../data-types';

@Injectable({
  providedIn: 'root'
})
export class AdminService {

  private responseMessageSource = new BehaviorSubject<string>('');
  responseMessage = this.responseMessageSource.asObservable();

  constructor(private networkService: NetworkService, private http: HttpClient) { }

  pdfUpload(networkPdfUploadRequest: NetworkPdfUploadRequest): any {
    const formData = new FormData();
    formData.append('title', networkPdfUploadRequest.title);
    formData.append('file', networkPdfUploadRequest.file);
    this.http.post< any >(environment.apiUrl + 'files/',
      formData).pipe(catchError(this.networkService.handleError)).subscribe(
      (data: any) => {
        this.http.post< NetworkPdfUploadResponse >(environment.apiUrl + 'addfile/', {
          data}, {
          withCredentials: true,
          headers: new HttpHeaders({
            'Content-Type': 'application/json'
          })
        }).subscribe(
          (networkPdfUploadResponse: NetworkPdfUploadResponse) => {
            if (networkPdfUploadResponse.success) {
              this.responseMessageSource.next('File was successfully uploaded');
            } else {
              console.log('Error when uploading pdf, please contact technical support');
            }
          },
          (error: any) => {
            console.log(error);
          }
        );
      },
      (error: any) => {
        console.log(error);
      }
    );
  }
}
