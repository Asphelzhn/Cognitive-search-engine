import {Component, Input, OnInit} from '@angular/core';
import {SearchService} from '../../../network-services/search.service';

@Component({
  selector: 'app-related-result-bar',
  templateUrl: './related-result-bar.component.html',
  styleUrls: ['./related-result-bar.component.scss']
})
export class RelatedResultBarComponent implements OnInit {
  @Input() sentence: string;

  constructor(private searchService: SearchService) { }

  ngOnInit() {
  }

  search(): void {
    this.searchService.search(this.sentence);
  }

}
