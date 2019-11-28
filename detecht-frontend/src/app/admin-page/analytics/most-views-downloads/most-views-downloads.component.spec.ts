import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MostViewsDownloadsComponent } from './most-views-downloads.component';

describe('MostViewsDownloadsComponent', () => {
  let component: MostViewsDownloadsComponent;
  let fixture: ComponentFixture<MostViewsDownloadsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MostViewsDownloadsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MostViewsDownloadsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
