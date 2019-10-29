import {Component, OnInit, Input} from '@angular/core';
import {SearchResponse} from '../../../data-types';
import {environment} from '../../../../environments/environment';
import {MatDialog, MatDialogConfig} from '@angular/material';
import {SentenceHitsComponent} from '../sentence-hits/sentence-hits.component';
import {PreviewMessageService} from '../../../message-services/preview-message.service';

@Component({
  selector: 'app-result-bar',
  templateUrl: './result-bar.component.html',
  styleUrls: ['./result-bar.component.scss']
})
export class ResultBarComponent implements OnInit {

  staticUrl: string;
  showPreview: boolean;
  showSentences: boolean;

  @Input() result: SearchResponse;

  constructor(
    public dialog: MatDialog,
    private previewData: PreviewMessageService
  ) {
  }

  openDialog() {
    const dialogConfig = new MatDialogConfig();
    dialogConfig.autoFocus = true;
    dialogConfig.disableClose = false;
    const dialogRef = this.dialog.open(SentenceHitsComponent, {
      data: {resultValue: this.result}
    });
    dialogRef.afterClosed().subscribe(value => {
      this.result = value.data;
      this.showPreview = true;
    });
  }

  ngOnInit() {
    this.staticUrl = environment.staticUrl;
    this.showSentences = false;
    this.previewData.currentMessage.subscribe(showPreview => this.showPreview = showPreview);

  }

}
