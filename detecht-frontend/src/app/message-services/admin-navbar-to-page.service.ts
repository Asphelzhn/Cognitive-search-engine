import { Injectable } from '@angular/core';
import {BehaviorSubject} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AdminNavbarToPageService {

  private pageSource = new BehaviorSubject<string>('analytics');
  page = this.pageSource.asObservable();

  constructor() { }

  changePage(page: string): void {
    this.pageSource.next(page);
  }
}
