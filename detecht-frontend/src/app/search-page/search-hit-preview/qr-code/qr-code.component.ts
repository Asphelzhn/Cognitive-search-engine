import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-qr-code',
  templateUrl: './qr-code.component.html',
  styleUrls: ['./qr-code.component.scss']
})
export class QrCodeComponent implements OnInit {
  @Input() url: string;
  constructor() { }

  ngOnInit() {
  }
}
