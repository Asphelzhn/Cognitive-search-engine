import { Injectable } from '@angular/core';
import {NetworkService} from './network.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {catchError} from 'rxjs/operators';
import {BehaviorSubject} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RelatedSearchesService {

  private relatedSearchesSource = new BehaviorSubject<string[]>([]);
  relatedSearches = this.relatedSearchesSource.asObservable();

  constructor(private networkService: NetworkService, private http: HttpClient) { }

  update(query: string): void {
    this.http.post<any>(environment.apiUrl + 'relatedsearches/', {query}, {
      withCredentials: true,
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })}
    ).pipe(catchError(this.networkService.handleError)).subscribe(
      (data) => {
        console.log(data);
        if (data.success) {
          this.relatedSearchesSource.next(data.searches);
        } else {
          console.log('Error in related searches');
        }
      },
      (error) => {
        console.log(error);
      }
    );
  }
}
