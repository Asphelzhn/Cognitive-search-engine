import { TestBed } from '@angular/core/testing';

import { RelatedSearchesService } from './related-searches.service';

describe('RelatedSearchesService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: RelatedSearchesService = TestBed.get(RelatedSearchesService);
    expect(service).toBeTruthy();
  });
});
