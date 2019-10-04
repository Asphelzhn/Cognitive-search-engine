import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.scss']
})
export class SearchBarComponent implements OnInit {

  private searchString: string;

  search(): void {
    console.log('Searching for: ' + this.searchString);
  }



  constructor() { }

  ngOnInit() {
  }

}
