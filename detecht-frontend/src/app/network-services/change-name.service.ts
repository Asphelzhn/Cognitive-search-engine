import { Injectable } from '@angular/core';
import {NetworkService} from './network.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {NetworkChangeNameRequest} from './network-data-types';
import {environment} from '../../environments/environment';
import {catchError} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ChangeNameService {

  constructor(private networkService: NetworkService, private http: HttpClient) { }

  changeName(data: NetworkChangeNameRequest): void {
    this.http.post(environment.apiUrl + 'changename/', JSON.stringify(data), {
      withCredentials: true,
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })}
    ).pipe(catchError(this.networkService.handleError)).subscribe();
  }
}
