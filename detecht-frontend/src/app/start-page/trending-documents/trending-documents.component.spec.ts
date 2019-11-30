import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TrendingDocumentsComponent } from './trending-documents.component';

describe('TrendingDocumentsComponent', () => {
  let component: TrendingDocumentsComponent;
  let fixture: ComponentFixture<TrendingDocumentsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TrendingDocumentsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TrendingDocumentsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
