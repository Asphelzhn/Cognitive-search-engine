import {Component, OnInit, Output, EventEmitter} from '@angular/core';
import {Router} from '@angular/router';


@Component({
  selector: 'app-uploaded-file',
  templateUrl: './uploaded-file.component.html',
  styleUrls: ['./uploaded-file.component.scss']
})
export class UploadedFileComponent implements OnInit {

  constructor(
    private router: Router
  ) { }

  ngOnInit() {
  }
  deletePDF(fileName: string): void {
    console.log('Delete ' + fileName);
  }


}
