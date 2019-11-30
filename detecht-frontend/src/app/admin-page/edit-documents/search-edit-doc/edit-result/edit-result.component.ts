import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-edit-result',
  templateUrl: './edit-result.component.html',
  styleUrls: ['./edit-result.component.scss']
})
export class EditResultComponent implements OnInit {

  @Input() title: string;
  @Input() abstract: string;
  icon: string;
  constructor() { }

  ngOnInit() {
    const index = Math.round(Math.random() * 2 + 1);
    this.icon = 'static/assets/admin-page/color-bar-' + index + '-icon.png';
  }

}
