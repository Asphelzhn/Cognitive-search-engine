import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchEditDocComponent } from './search-edit-doc.component';

describe('SearchEditDocComponent', () => {
  let component: SearchEditDocComponent;
  let fixture: ComponentFixture<SearchEditDocComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SearchEditDocComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchEditDocComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
