import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-result-bar',
  templateUrl: './result-bar.component.html',
  styleUrls: ['./result-bar.component.scss']
})
export class ResultBarComponent implements OnInit {

  @Input('result') result: any;

  constructor() { }

  ngOnInit() {
  }

}
