import { Injectable } from '@angular/core';
import {TrendingDocumentsResponse} from '../data-types';
import {BehaviorSubject, Observable} from 'rxjs';
import {NetworkService} from './network.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {catchError} from 'rxjs/operators';
import { NetworkTrendingDocumentsResponse} from './network-data-types'; // NetworkTrendingDocumentsRequest, prob not need.

@Injectable({
  providedIn: 'root'
})
export class TrendingDocumentService {


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

