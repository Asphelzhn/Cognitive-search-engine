import {Component, Input, OnInit} from '@angular/core';
import {DeletePdfService} from '../../../../network-services/delete-pdf.service';
import {Router} from '@angular/router';
import {SearchService} from '../../../../network-services/search.service';

@Component({
  selector: 'app-edit-result',
  templateUrl: './edit-result.component.html',
  styleUrls: ['./edit-result.component.scss']
})
export class EditResultComponent implements OnInit {

  @Input() title: string;
  @Input() abstract: string;
  @Input() query: string;
  icon: string;
  constructor(private deletePdfService: DeletePdfService, private searchService: SearchService, private router: Router) { }

  ngOnInit() {
    const index = Math.round(Math.random() * 2 + 1);
    this.icon = 'static/assets/admin-page/color-bar-' + index + '-icon.png';
  }

  delete() {
    this.deletePdfService.deletePdf(this.title).subscribe(
      response => console.log(response)
    );
    this.searchService.search(this.query);
  }

}
