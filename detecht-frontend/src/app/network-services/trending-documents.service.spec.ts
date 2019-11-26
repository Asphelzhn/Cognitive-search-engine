import { TestBed } from '@angular/core/testing';

import { TrendingDocumentsService } from './trending-documents.service';

describe('TrendingDocumentsService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: TrendingDocumentsService = TestBed.get(TrendingDocumentsService);
    expect(service).toBeTruthy();
  });
});
