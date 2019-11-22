import {Component, OnInit, Input} from '@angular/core';
import {SearchResponse} from '../../../data-types';
import {environment} from '../../../../environments/environment';
import {MatDialog, MatDialogConfig} from '@angular/material';
import {SearchHitPreviewComponent} from '../../search-hit-preview/search-hit-preview.component';
import {PreviewMessageService} from '../../../message-services/preview-message.service';
import { FileSaverModule } from 'ngx-filesaver';
import {SearchHitPreviewService} from '../../../message-services/search-hit-preview.service';


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
    private previewData: PreviewMessageService,
    private searchHitPreviewService: SearchHitPreviewService
  ) {
  }

  openDialog() {
    this.searchHitPreviewService.changeResult(this.result);
    // const dialogConfig = new MatDialogConfig();
    // dialogConfig.autoFocus = true;
    // dialogConfig.disableClose = false;
    // const dialogRef = this.dialog.open(SearchHitPreviewComponent, {
    //   data: {resultValue: this.results}
    // });
    // dialogRef.afterClosed().subscribe(value => {
    //   this.results = value.data;
    // });
  }

  ngOnInit() {
    this.staticUrl = environment.staticUrl;
    this.showSentences = false;
    this.previewData.currentMessage.subscribe(showPreview => this.showPreview = showPreview);

  }

}
