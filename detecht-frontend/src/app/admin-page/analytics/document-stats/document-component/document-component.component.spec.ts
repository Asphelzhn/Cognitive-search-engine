import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DocumentComponentComponent } from './document-component.component';

describe('DocumentComponentComponent', () => {
  let component: DocumentComponentComponent;
  let fixture: ComponentFixture<DocumentComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DocumentComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DocumentComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
