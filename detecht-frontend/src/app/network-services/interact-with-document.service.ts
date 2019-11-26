import { Injectable } from '@angular/core';
import {NetworkService} from './network.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {catchError} from 'rxjs/operators';
import {NetworkInteractWithDocumentRequest} from './network-data-types';

@Injectable({
  providedIn: 'root'
})
export class InteractWithDocumentService {

  constructor(private networkService: NetworkService, private http: HttpClient) { }

  previewDocument(data: NetworkInteractWithDocumentRequest): void {
    data.type = 'preview';
    this.http.post(environment.apiUrl + 'trendingdocuments/', {data}, {
      withCredentials: true,
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).pipe(catchError(this.networkService.handleError));
  }
}
