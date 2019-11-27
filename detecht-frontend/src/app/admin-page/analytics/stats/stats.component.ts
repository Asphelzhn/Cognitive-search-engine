import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-stats',
  templateUrl: './stats.component.html',
  styleUrls: ['./stats.component.scss']
})
export class StatsComponent implements OnInit {
  @Input() downloads: number;
  @Input() favorites: number;
  @Input() documents: number;

  constructor() { }

  ngOnInit() {
  }

}
