import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TrendingDocumentComponent } from './trending-document.component';

describe('TrendingDocumentComponent', () => {
  let component: TrendingDocumentComponent;
  let fixture: ComponentFixture<TrendingDocumentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TrendingDocumentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TrendingDocumentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
