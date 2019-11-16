import {Component, OnInit} from '@angular/core';
import {AdminService} from '../../network-services/admin.service';

@Component({
  selector: 'app-analytics',
  templateUrl: './analytics.component.html',
  styleUrls: ['./analytics.component.scss']
})
export class AnalyticsComponent implements OnInit {

  // pdfs: any[];

  constructor(private adminService: AdminService) { }

  ngOnInit() {
    // this.adminService.getAllPdf().subscribe(pdfs => this.pdfs = pdfs);
  }

  deletePDF(fileName: string): void {
    console.log('Delete ' + fileName);
  }
}
