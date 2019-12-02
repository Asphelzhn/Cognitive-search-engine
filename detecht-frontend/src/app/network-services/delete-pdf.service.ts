import { Injectable } from '@angular/core';
import {NetworkService} from './network.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {catchError} from 'rxjs/operators';
import {environment} from '../../environments/environment';
import {Observable} from 'rxjs';
import {NetworkSuccessResponse} from './network-data-types';

@Injectable({
  providedIn: 'root'
})
export class DeletePdfService {

  constructor(private networkService: NetworkService, private http: HttpClient) { }

  deletePdf(pdfName: string): Observable<NetworkSuccessResponse> {
    return this.http.post<NetworkSuccessResponse>(environment.apiUrl + 'deletepdf/', {pdfName}, {
      withCredentials: true,
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })}
    ).pipe(catchError(this.networkService.handleError));
  }
}
