import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SentenceHitsComponent } from './sentence-hits.component';

describe('SentenceHitsComponent', () => {
  let component: SentenceHitsComponent;
  let fixture: ComponentFixture<SentenceHitsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SentenceHitsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SentenceHitsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
