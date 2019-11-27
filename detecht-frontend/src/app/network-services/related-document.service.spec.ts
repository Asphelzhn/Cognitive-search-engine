import { TestBed } from '@angular/core/testing';

import { RelatedDocumentService } from './related-document.service';

describe('RelatedDocumentService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: RelatedDocumentService = TestBed.get(RelatedDocumentService);
    expect(service).toBeTruthy();
  });
});
