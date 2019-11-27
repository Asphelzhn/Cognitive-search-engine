import { Injectable } from '@angular/core';
import {NetworkService} from './network.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {catchError} from 'rxjs/operators';
import {NetworkGetAnalyticsResponse} from './network-data-types';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GetAnalyticsService {

  constructor(private networkService: NetworkService, private http: HttpClient) { }

  getAnalytics(): Observable<NetworkGetAnalyticsResponse> {
    return this.http.get<NetworkGetAnalyticsResponse>(environment.apiUrl + 'getanalytics/', {
      withCredentials: true,
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })}
    ).pipe(catchError(this.networkService.handleError));
  }
}
