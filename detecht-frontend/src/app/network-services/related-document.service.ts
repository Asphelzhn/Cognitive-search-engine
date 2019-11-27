import { Injectable } from '@angular/core';
import {NetworkService} from './network.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {NetworkRelatedDocumentRequest, NetworkRelatedDocumentResponse} from './network-data-types';
import {Observable} from 'rxjs';
import {environment} from '../../environments/environment';
import {stringify} from 'querystring';
import {catchError} from 'rxjs/operators';
import {resolveFileWithPostfixes} from "@angular/compiler-cli/ngcc/src/utils";

@Injectable({
  providedIn: 'root'
})
export class RelatedDocumentService {

  constructor(private networkService: NetworkService, private http: HttpClient) { }

  relatedDocument(data: NetworkRelatedDocumentRequest): Observable<NetworkRelatedDocumentResponse> {
    return this.http.post<NetworkRelatedDocumentResponse>(environment.apiUrl + 'relateddocuments/', JSON.stringify(data), {
      withCredentials: true,
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })}
      ).pipe(catchError(this.networkService.handleError));
  }
}
