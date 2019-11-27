import {Component, Input, OnInit, Pipe, PipeTransform} from '@angular/core';
import {Pdf, SearchResponse} from '../../../data-types';
import {SearchService} from '../../../network-services/search.service';

@Component({
  selector: 'app-document-stats',
  templateUrl: './document-stats.component.html',
  styleUrls: ['./document-stats.component.scss']
})
export class DocumentStatsComponent implements OnInit {

  pdfs: SearchResponse[];
  searchString: string;
  constructor(private searchService: SearchService) { }

  ngOnInit() {
    this.searchString = '';
    this.searchService.searchResponse.subscribe(searchResult => this.pdfs = searchResult);
  }

  search() {
    this.searchService.search(this.searchString);
  }

}
