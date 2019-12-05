import {Component, Input, Output, EventEmitter, OnInit} from '@angular/core';
import {DeletePdfService} from '../../../../network-services/delete-pdf.service';
import {Router} from '@angular/router';
import {SearchService} from '../../../../network-services/search.service';
import {SearchResponse} from '../../../../data-types';

@Component({
  selector: 'app-edit-result',
  templateUrl: './edit-result.component.html',
  styleUrls: ['./edit-result.component.scss']
})
export class EditResultComponent implements OnInit {

  @Input() result: SearchResponse;
  @Input() query: string;
  icon: string;
  @Output() pdfNameEvent = new EventEmitter<SearchResponse>();
  hide = false;

  constructor(private deletePdfService: DeletePdfService, private searchService: SearchService, private router: Router) { }

  ngOnInit() {
    const index = Math.round(Math.random() * 2 + 1);
    this.icon = 'static/assets/admin-page/color-bar-' + index + '-icon.png';
  }

  delete() {
    this.deletePdfService.deletePdf(this.result.name).subscribe(
      (response) => {
        this.hide = true;
      }
    );
  }

  editDocument() {
    this.pdfNameEvent.emit(this.result);
  }

}
