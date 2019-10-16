import { Component, OnInit, Input } from '@angular/core';
import {SearchResponse} from '../../../data-types';
import {environment} from '../../../../environments/environment';
import {MatDialog, MatDialogConfig} from '@angular/material';
import {SentenceHitsComponent} from '../../sentence-hits/sentence-hits.component';

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

  constructor(private dialog: MatDialog) {}

  openDialog() {
    const dialogConfig = new MatDialogConfig();

    dialogConfig.autoFocus = true;

    this.dialog.open(SentenceHitsComponent, dialogConfig);

  }


  ngOnInit() {
    this.staticUrl = environment.staticUrl;
    this.showPreview = false;
    this.showSentences = false;
  }

}
