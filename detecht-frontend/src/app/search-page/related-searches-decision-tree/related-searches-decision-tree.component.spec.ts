import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RelatedSearchesDecisionTreeComponent } from './related-searches-decision-tree.component';

describe('RelatedSearchesDecisionTreeComponent', () => {
  let component: RelatedSearchesDecisionTreeComponent;
  let fixture: ComponentFixture<RelatedSearchesDecisionTreeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RelatedSearchesDecisionTreeComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RelatedSearchesDecisionTreeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
