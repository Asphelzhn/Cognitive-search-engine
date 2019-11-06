import {Component, Inject, OnInit} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from '@angular/material';
import {environment} from '../../../../environments/environment';
import {SearchResponse} from '../../../data-types';
import {SearchService} from '../../../network-services/search.service';
import {PreviewMessageService} from '../../../message-services/preview-message.service';

@Component({
  selector: 'app-sentence-hits',
  templateUrl: './sentence-hits.component.html',
  styleUrls: ['./sentence-hits.component.scss']
})
export class SentenceHitsComponent implements OnInit {
  result: SearchResponse;
  staticUrl: string;
  showPreview: boolean;
  rightSentence: string;

  constructor(
    public dialogRef: MatDialogRef<SentenceHitsComponent>,
    private searchService: SearchService,
    private previewData: PreviewMessageService,
    @Inject(MAT_DIALOG_DATA) public data: any
  ) {
    this.result = data.resultValue;
  }

  close() {
    this.dialogRef.close({event: 'close', data: this.result});
  }

  ngOnInit() {
    this.staticUrl = environment.staticUrl;
    this.previewData.currentMessage.subscribe(showPreview => this.showPreview = showPreview);
  }

  displayPreview(sentence: string): void {
    this.showPreview = true;
    this.rightSentence = sentence;
  }

}
