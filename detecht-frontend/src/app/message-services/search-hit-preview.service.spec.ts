import { TestBed } from '@angular/core/testing';

import { SearchHitPreviewService } from './search-hit-preview.service';

describe('SearchHitPreviewService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: SearchHitPreviewService = TestBed.get(SearchHitPreviewService);
    expect(service).toBeTruthy();
  });
});
