import { TestBed } from '@angular/core/testing';

import { InteractWithDocumentService } from './interact-with-document.service';

describe('InteractWithDocumentService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: InteractWithDocumentService = TestBed.get(InteractWithDocumentService);
    expect(service).toBeTruthy();
  });
});
