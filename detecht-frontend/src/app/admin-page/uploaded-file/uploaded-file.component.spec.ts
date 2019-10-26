import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UploadedFileComponent } from './uploaded-file.component';

describe('UploadedFileComponent', () => {
  let component: UploadedFileComponent;
  let fixture: ComponentFixture<UploadedFileComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UploadedFileComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UploadedFileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
