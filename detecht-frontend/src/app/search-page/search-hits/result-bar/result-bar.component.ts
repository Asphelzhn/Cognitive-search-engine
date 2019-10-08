import { Component, OnInit, Input } from '@angular/core';
import {SearchResponse} from '../../../data-types';
import {environment} from '../../../../environments/environment';

@Component({
  selector: 'app-result-bar',
  templateUrl: './result-bar.component.html',
  styleUrls: ['./result-bar.component.scss']
})
export class ResultBarComponent implements OnInit {

  staticUrl: string;

  @Input() result: SearchResponse;

  constructor() { }

  ngOnInit() {
    this.staticUrl = environment.staticUrl;
  }

}
