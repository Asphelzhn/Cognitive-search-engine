import {EventEmitter, Injectable} from '@angular/core';
import {BehaviorSubject, Subscription} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PreviewMessageService {
  private messageSource = new BehaviorSubject<boolean>(false);
  currentMessage = this.messageSource.asObservable();

  constructor() { }

  changeMessage(showPreview: boolean) {
    this.messageSource.next(showPreview);
  }
}
