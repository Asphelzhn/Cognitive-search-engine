import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-document-stats',
  templateUrl: './document-stats.component.html',
  styleUrls: ['./document-stats.component.scss']
})
export class DocumentStatsComponent implements OnInit {

    showViews: boolean;
  constructor() { }

  ngOnInit() {
    this.showViews = true;
  }

}
