import { Injectable } from '@angular/core';
import {BehaviorSubject} from 'rxjs';
import {SearchResponse} from '../data-types';

@Injectable({
  providedIn: 'root'
})
export class SearchHitPreviewService {

  private resultSource = new BehaviorSubject<SearchResponse>(undefined);
  result = this.resultSource.asObservable();

  constructor() { }

  changeResult(result: SearchResponse): void {
    this.resultSource.next(result);
  }

}
