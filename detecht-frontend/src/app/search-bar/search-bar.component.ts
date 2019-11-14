import {Component, Input, OnInit} from '@angular/core';
import {Router} from '@angular/router';
import {SearchService} from '../network-services/search.service';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.scss']
})
export class SearchBarComponent implements OnInit {

  constructor(private searchService: SearchService, private router: Router) { }

  searchString: string;
  @Input() changePage: boolean;

  ngOnInit() {
    this.searchService.currentSearch.subscribe(query => this.searchString = query);
  }

  search(): void {
    console.log('Searching for: ' + this.searchString);
    this.searchService.search(this.searchString);
    if (this.changePage) {
      this.router.navigateByUrl('search');
    }
  }

}
