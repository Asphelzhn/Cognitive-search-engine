import { Injectable } from '@angular/core';
import {AskQuestion, SearchResponse, Spellcheck} from '../data-types';
import {BehaviorSubject, Observable} from 'rxjs';
import {NetworkService} from './network.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {catchError} from 'rxjs/operators';
import {
  GetDocResponse,
  NetworkAbstractRequest,
  NetworkAbstractResponse,
  NetworkAutoCompleteResponse,
  NetworkSearchResponse
} from './network-data-types';

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  private searchResponseSource = new BehaviorSubject<SearchResponse[]>([]);
  searchResponse = this.searchResponseSource.asObservable();

  private currentSearchSource = new BehaviorSubject<string>('');
  currentSearch = this.currentSearchSource.asObservable();

  private spellcheckSource = new BehaviorSubject<Spellcheck[]>([]);
  spellcheck = this.spellcheckSource.asObservable();

  private totalResultsSource = new BehaviorSubject<number>(0);
  totalResults = this.totalResultsSource.asObservable();

  constructor(private networkService: NetworkService, private http: HttpClient) { }

  abstract(networkAbstractRequest: NetworkAbstractRequest): Observable<NetworkAbstractResponse> {
    return this.http.post< NetworkAbstractResponse >(environment.apiUrl + 'getabstract/', {
      networkAbstractRequest}, {
      withCredentials: true,
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).pipe(catchError(this.networkService.handleError));
  }

  search(query: string, askQuestions: AskQuestion[] = []): void {
    this.currentSearchSource.next(query);

    this.http.post< NetworkSearchResponse >(environment.apiUrl + 'search/', {
      query, askQuestions}, {
      withCredentials: true,
        headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).pipe(catchError(this.networkService.handleError)).subscribe(
      (data: NetworkSearchResponse) => {
        if (data.success) {
          const newSearchResponse: SearchResponse[] = [];
          for (const content of data.content) {
            newSearchResponse.push(new SearchResponse(content.pdfTitle, content.pdfName, content.keywords));
          }

          this.searchResponseSource.next(newSearchResponse);
          this.totalResultsSource.next(data.totalResult);
          const newSpellcheck: Spellcheck[] = [];
          console.log(data.spellcheck);
          for (const spellcheck of data.spellcheck) {
            newSpellcheck.push(new Spellcheck(spellcheck.word, spellcheck.spellcheck));
          }
          this.spellcheckSource.next(newSpellcheck);
        } else {
          console.log('Error when getting schedule, please refresh the results');
        }
      },
      (error: any) => {
        console.log(error);
      }
    );
  }

  autocomplete(query: string): Observable<NetworkAutoCompleteResponse> {
    return this.http.post< NetworkAutoCompleteResponse >(environment.apiUrl + 'getautocomplete/', {
      query}, {
      withCredentials: true,
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).pipe(catchError(this.networkService.handleError));
  }

  getDoc(pdfName: string, query: string): Observable<GetDocResponse> {
    return this.http.post< GetDocResponse >(environment.apiUrl + 'getdoc/', {
      pdfName, query}, {
      withCredentials: true,
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).pipe(catchError(this.networkService.handleError));
  }

}
