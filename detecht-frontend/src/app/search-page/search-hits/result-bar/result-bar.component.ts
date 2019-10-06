import { Component, OnInit, Input } from '@angular/core';
import {SearchResponse} from '../../../data-types';

@Component({
  selector: 'app-result-bar',
  templateUrl: './result-bar.component.html',
  styleUrls: ['./result-bar.component.scss']
})
export class ResultBarComponent implements OnInit {

  @Input() result: SearchResponse;

  constructor() { }

  ngOnInit() {
  }

}
