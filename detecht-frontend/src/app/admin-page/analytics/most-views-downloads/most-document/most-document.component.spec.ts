import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MostDocumentComponent } from './most-document.component';

describe('MostDocumentComponent', () => {
  let component: MostDocumentComponent;
  let fixture: ComponentFixture<MostDocumentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MostDocumentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MostDocumentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
