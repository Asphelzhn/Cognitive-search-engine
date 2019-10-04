import { Injectable } from '@angular/core';
import {SearchResult} from '../data-types';
import {BehaviorSubject} from 'rxjs';
import {NetworkService} from './network.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {catchError} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  private searchResultSource = new BehaviorSubject<SearchResult[]>([]);
  searchResult = this.searchResultSource.asObservable();

  private currentSearchSource = new BehaviorSubject<string>('');
  currentSearch = this.currentSearchSource.asObservable();

  constructor(private networkService: NetworkService, private http: HttpClient) { }


  search(query: string): void {
    this.currentSearchSource.next(query);

    this.http.post< boolean >(environment.apiUrl + 'schedule/insert/activities', {
      query}, {
      withCredentials: true,
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).pipe(catchError(this.networkService.handleError)).subscribe(
      (data: boolean) => {
        if (!data) {
          console.log('Error when getting schedule, please refresh the page');
        }
      },
      (error: any) => {
        console.log(error);
      }
    );
  }
}
