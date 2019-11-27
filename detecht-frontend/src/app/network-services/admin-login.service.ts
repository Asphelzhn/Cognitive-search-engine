import { Injectable } from '@angular/core';
import {NetworkService} from './network.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {NetworkAdminLoginRequest, NetworkAdminLoginResponse} from './network-data-types';
import {Observable} from 'rxjs';
import {environment} from '../../environments/environment';
import {catchError} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AdminLoginService {

  constructor(private networkService: NetworkService, private http: HttpClient) { }

  relatedDocument(data: NetworkAdminLoginRequest): Observable<NetworkAdminLoginResponse> {
    return this.http.post<NetworkAdminLoginResponse>(environment.apiUrl + 'relateddocuments/', JSON.stringify(data), {
      withCredentials: true,
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })}
    ).pipe(catchError(this.networkService.handleError));
  }
}
