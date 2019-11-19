import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchHitPreviewComponent } from './search-hit-preview.component';

describe('SearchHitPreviewComponent', () => {
  let component: SearchHitPreviewComponent;
  let fixture: ComponentFixture<SearchHitPreviewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SearchHitPreviewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchHitPreviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
