import {Component, Inject, Input, OnInit} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from '@angular/material';
import {environment} from '../../../environments/environment';
import {SearchResponse} from '../../data-types';
import {SearchService} from '../../network-services/search.service';
import {PreviewMessageService} from '../../message-services/preview-message.service';
import {NetworkAbstractRequest, NetworkAbstractResponse, NetworkSearchResponse} from '../../network-services/network-data-types';
import {SearchHitPreviewService} from '../../message-services/search-hit-preview.service';

@Component({
  selector: 'app-search-hit-preview',
  templateUrl: './search-hit-preview.component.html',
  styleUrls: ['./search-hit-preview.component.scss']
})
export class SearchHitPreviewComponent implements OnInit {
  @Input() result: SearchResponse;
  staticUrl: string;
  showPreview: boolean;
  rightSentence: string;
  sentences: string[];
  query: string;
  liked: boolean;

  constructor(
    private searchService: SearchService,
    private previewData: PreviewMessageService,
    private searchHitPreviewService: SearchHitPreviewService
  ) { }

  close() {
    this.searchHitPreviewService.changeResult(undefined);
  }

  ngOnInit() {
    this.searchService.currentSearch.subscribe(query => this.query = query);
    this.searchService.abstract(new NetworkAbstractRequest(this.query, this.result.name)).subscribe(
      (data: NetworkAbstractResponse) => {
        if (data.success) {
          this.sentences = [];
          for (const abstract of data.abstracts) {
            this.sentences.push(abstract.sentence);
          }
          console.log(this.sentences);
        } else {
          console.log('Error when getting schedule, please refresh the results');
        }
      },
      (error: any) => {
        console.log(error);
      }
    );

    this.staticUrl = environment.staticUrl;
    this.previewData.currentMessage.subscribe(showPreview => this.showPreview = showPreview);
    this.liked = false;
  }

  displayPreview(sentence: string): void {
    this.showPreview = true;
    this.rightSentence = sentence;
  }

}
