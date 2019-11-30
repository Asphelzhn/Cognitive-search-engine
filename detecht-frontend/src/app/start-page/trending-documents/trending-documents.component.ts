import { Component, OnInit } from '@angular/core';
import {SearchResponse, TrendingDocumentsResponse} from '../../data-types';
import {TrendingDocumentsService} from '../../network-services/trending-documents.service';
import {NetworkSearchResponse, NetworkTrendingDocumentsResponse} from '../../network-services/network-data-types';

@Component({
  selector: 'app-trending-documents',
  templateUrl: './trending-documents.component.html',
  styleUrls: ['./trending-documents.component.scss']
})
export class TrendingDocumentsComponent implements OnInit {

  trendingDocs: TrendingDocumentsResponse[];

  constructor(private trendingDocumentsService: TrendingDocumentsService) { }

  ngOnInit() {
    this.trendingDocumentsService.trendingDocuments(6).subscribe(
      (data: NetworkTrendingDocumentsResponse) => {
        this.trendingDocs = [];
        for (const document of data.content) {
          this.trendingDocs.push(new TrendingDocumentsResponse(document.pdf_name, document.trend_score, document.title));
        }
      },
      (error: any) => {
        console.log(error);
      }
    );
  }

}
