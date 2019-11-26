import { Injectable } from '@angular/core';
import {NetworkService} from './network.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';
import {NetworkTrendingDocumentsResponse} from './network-data-types';
import {environment} from '../../environments/environment';
import {catchError} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class TrendingDocumentsService {

  constructor(private networkService: NetworkService, private http: HttpClient) { }

  trendingDocuments(size: number): Observable<NetworkTrendingDocumentsResponse> {
    return this.http.post<NetworkTrendingDocumentsResponse>(environment.apiUrl + 'trendingdocuments/', {size}, {
      withCredentials: true,
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).pipe(catchError(this.networkService.handleError));
  }

}
