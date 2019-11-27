import { Injectable } from '@angular/core';
import {NetworkService} from './network.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {NetworkFavoriteDocumentRequest} from './network-data-types';
import {environment} from '../../environments/environment';
import {catchError} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class UserFavoriteService {

  constructor(private networkService: NetworkService, private http: HttpClient) { }

  favoriteDocument(data: NetworkFavoriteDocumentRequest): any {
    console.log(data);
    this.http.post<any>(environment.apiUrl + 'userfavorite/', JSON.stringify(data), {
      withCredentials: true,
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).pipe(catchError(this.networkService.handleError)).subscribe(
      response => console.log(response)
    );
  }
}
