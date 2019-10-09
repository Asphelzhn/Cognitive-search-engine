import {Component, NgModule, OnInit} from '@angular/core';
import { Router } from '@angular/router';
import { UploadFileComponent } from './upload-file/upload-file.component';

@Component({
  selector: 'app-admin-page',
  templateUrl: './admin-page.component.html',
  styleUrls: ['./admin-page.component.scss']
})


@NgModule({
  imports: [],
  declarations: []
})

export class AdminPageComponent implements OnInit {

  constructor(
    private router: Router
  ) { }

  ngOnInit() {
  }
}
