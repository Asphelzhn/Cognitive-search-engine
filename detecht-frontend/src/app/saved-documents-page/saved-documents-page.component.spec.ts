import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SavedDocumentsPageComponent } from './saved-documents-page.component';

describe('SavedDocumentsPageComponent', () => {
  let component: SavedDocumentsPageComponent;
  let fixture: ComponentFixture<SavedDocumentsPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SavedDocumentsPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SavedDocumentsPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
