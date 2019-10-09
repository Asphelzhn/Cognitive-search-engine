import {Component, Input, OnInit} from '@angular/core';
import {SearchResponse} from '../../../data-types';
import {SearchService} from '../../../network-services/search.service';

@Component({
  selector: 'app-related-result-bar',
  templateUrl: './related-result-bar.component.html',
  styleUrls: ['./related-result-bar.component.scss']
})
export class RelatedResultBarComponent implements OnInit {
  @Input() result: string;
  ngOnInit() {

  }

}
