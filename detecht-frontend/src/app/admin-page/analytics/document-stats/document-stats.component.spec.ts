import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DocumentStatsComponent } from './document-stats.component';

describe('DocumentStatsComponent', () => {
  let component: DocumentStatsComponent;
  let fixture: ComponentFixture<DocumentStatsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DocumentStatsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DocumentStatsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
