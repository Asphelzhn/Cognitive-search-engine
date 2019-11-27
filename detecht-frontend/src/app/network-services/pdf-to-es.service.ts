import { Injectable } from '@angular/core';
import {NetworkService} from './network.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {NetworkAdminLoginRequest} from "./network-data-types";
import {environment} from '../../environments/environment';
import {catchError} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class PdfToEsService {

  constructor(private networkService: NetworkService, private http: HttpClient) { }

  // returns {"key": xxxx } when login is correct.
  // Otherwise see: https://sunscrapers.com/blog/django-rest-framework-login-and-authentication/
  pdfToEs(): any {
    this.http.get<any>(environment.apiUrl + 'pdftoes/', {
      withCredentials: true,
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })}
    ).pipe(catchError(this.networkService.handleError)).subscribe(
      response => console.log(response)
    );
  }
}
