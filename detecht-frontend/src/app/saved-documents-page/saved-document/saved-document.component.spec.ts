import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SavedDocumentComponent } from './saved-document.component';

describe('SavedDocumentComponent', () => {
  let component: SavedDocumentComponent;
  let fixture: ComponentFixture<SavedDocumentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SavedDocumentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SavedDocumentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
