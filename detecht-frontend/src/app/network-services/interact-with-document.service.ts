import { Injectable } from '@angular/core';
import {NetworkService} from './network.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';
import {NetworkInteractWithDocumentRequest} from './network-data-types';
import {environment} from '../../environments/environment';
import {catchError} from 'rxjs/operators';
import {stringify} from "querystring";



@Injectable({
  providedIn: 'root'
})
export class InteractWithDocumentService {

  constructor(private networkService: NetworkService, private http: HttpClient) { }

  previewDocument(data: NetworkInteractWithDocumentRequest): any {
    data.type = 'Preview';
    this.http.post<any>(environment.apiUrl + 'interactwithdocument/', JSON.stringify(data), {
      withCredentials: true,
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).pipe(catchError(this.networkService.handleError)).subscribe(
      response => console.log(response)
    );
  }

  downloadDocument(data: NetworkInteractWithDocumentRequest): any {
    data.type = 'Download';
    this.http.post<any>(environment.apiUrl + 'interactwithdocument/', JSON.stringify(data), {
      withCredentials: true,
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).pipe(catchError(this.networkService.handleError)).subscribe(
      response => console.log(response)
    );
  }
}
