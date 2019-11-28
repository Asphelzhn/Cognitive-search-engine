import { Injectable } from '@angular/core';
import {BehaviorSubject} from 'rxjs';
import {Abstract, SearchResponse} from '../data-types';

@Injectable({
  providedIn: 'root'
})
export class SearchHitPreviewService {

  private resultSource = new BehaviorSubject<SearchResponse>(undefined);
  result = this.resultSource.asObservable();

  private abstractsSource = new BehaviorSubject<Abstract[]>([]);
  abstracts = this.abstractsSource.asObservable();

  constructor() { }

  changeResult(result: SearchResponse, abstracts: Abstract[]): void {
    this.resultSource.next(result);
    this.abstractsSource.next(abstracts);
  }

}
