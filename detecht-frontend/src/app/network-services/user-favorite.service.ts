import { Injectable } from '@angular/core';
import {NetworkService} from './network.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {NetworkFavoriteDocumentRequest, NetworkGetFavoriteDocumentsResponse, NetworkIsFavoriteResponse} from './network-data-types';
import {environment} from '../../environments/environment';
import {catchError} from 'rxjs/operators';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserFavoriteService {

  constructor(private networkService: NetworkService, private http: HttpClient) { }

  favoriteDocument(data: NetworkFavoriteDocumentRequest): any {
    this.http.post<any>(environment.apiUrl + 'userfavorite/', JSON.stringify(data), {
      withCredentials: true,
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).pipe(catchError(this.networkService.handleError)).subscribe(
      response => console.log(response)
    );
  }

  getFavoriteDocuments(data: number): Observable<NetworkGetFavoriteDocumentsResponse> {
    return this.http.post<NetworkGetFavoriteDocumentsResponse>(environment.apiUrl + 'getuserfavorites/', JSON.stringify(data), {
      withCredentials: true,
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).pipe(catchError(this.networkService.handleError));
  }

  isFavorite(data: NetworkFavoriteDocumentRequest): Observable<NetworkIsFavoriteResponse> {
    return this.http.post<NetworkIsFavoriteResponse>(environment.apiUrl + 'isfavorite/', JSON.stringify(data), {
      withCredentials: true,
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).pipe(catchError(this.networkService.handleError));
  }
}
