import {Component, Input, OnInit} from '@angular/core';
import {MatDialogRef} from '@angular/material';
import {environment} from '../../../environments/environment';
import {SearchResponse} from '../../data-types';
import {SearchService} from '../../network-services/search.service';

@Component({
  selector: 'app-sentence-hits',
  templateUrl: './sentence-hits.component.html',
  styleUrls: ['./sentence-hits.component.scss']
})
export class SentenceHitsComponent implements OnInit {
  results: SearchResponse[];
  showPreview: boolean;
  staticUrl: string;

  @Input() result: SearchResponse;

  constructor(
    private dialogRef: MatDialogRef<SentenceHitsComponent>,
    private searchService: SearchService

  ) { }

  close() {
    this.dialogRef.close();
  }

  ngOnInit() {
    this.showPreview = false;
    this.staticUrl = environment.staticUrl;
    this.searchService.searchResponse.subscribe(searchResult => this.results = searchResult);
  }

}
