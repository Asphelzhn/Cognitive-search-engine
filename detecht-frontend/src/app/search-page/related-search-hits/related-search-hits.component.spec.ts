import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RelatedSearchHitsComponent } from './related-search-hits.component';

describe('RelatedSearchHitsComponent', () => {
  let component: RelatedSearchHitsComponent;
  let fixture: ComponentFixture<RelatedSearchHitsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RelatedSearchHitsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RelatedSearchHitsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
