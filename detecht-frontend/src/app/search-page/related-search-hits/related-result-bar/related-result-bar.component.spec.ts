import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RelatedResultBarComponent } from './related-result-bar.component';

describe('RelatedResultBarComponent', () => {
  let component: RelatedResultBarComponent;
  let fixture: ComponentFixture<RelatedResultBarComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RelatedResultBarComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RelatedResultBarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
