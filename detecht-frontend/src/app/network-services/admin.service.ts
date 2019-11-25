import { Injectable } from '@angular/core';
import {NetworkService} from './network.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {NetworkPdfUploadResponse, NetworkPdfUploadRequest, NetworkGetAllPdfResponse} from './network-data-types';
import {environment} from '../../environments/environment';
import {catchError} from 'rxjs/operators';
import {BehaviorSubject, Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AdminService {

  private responseMessageSource = new BehaviorSubject<string>('');
  responseMessage = this.responseMessageSource.asObservable();

  constructor(private networkService: NetworkService, private http: HttpClient) { }


  getAllPdf(): Observable<any> {
    return this.http.get<any>(environment.apiUrl + 'files/', {
      withCredentials: true
    }).pipe(catchError(this.networkService.handleError));
  }

  pdfUpload(networkPdfUploadRequests: NetworkPdfUploadRequest[]): void {
    console.log(networkPdfUploadRequests);
    if (networkPdfUploadRequests.length > 0) {
      const formData = new FormData();
      const fileData = networkPdfUploadRequests.pop();
      formData.append('title', fileData.title);
      formData.append('file', fileData.file);
      this.http.post< any >(environment.apiUrl + 'files/',
        formData).pipe(catchError(this.networkService.handleError)).subscribe(
        (data: any) => {
          this.http.post< NetworkPdfUploadResponse >(environment.apiUrl + 'addfile/', {
            data}, {
            withCredentials: true,
            headers: new HttpHeaders({
              'Content-Type': 'application/json'
            })
          }).pipe(catchError(this.networkService.handleError)).subscribe(
            (networkPdfUploadResponse: NetworkPdfUploadResponse) => {
              if (networkPdfUploadResponse.success) {
                this.pdfUpload(networkPdfUploadRequests);
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
    } else {
      this.http.put<any>(environment.apiUrl + 'pdftoes/', {},
        {
          withCredentials: true,
          headers: new HttpHeaders({
            'Content-Type': 'application/json'
          })
        }
      ).pipe(catchError(this.networkService.handleError)).subscribe(
        (data: any) => {
          console.log('SUCCESS!!!');
          this.responseMessageSource.next('Files was successfully uploaded and processed');
        },
        (error: any) => {
          console.log(error);
        }
      );
    }

  }
}
