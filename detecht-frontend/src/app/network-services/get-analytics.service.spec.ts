import { TestBed } from '@angular/core/testing';

import { GetAnalyticsService } from './get-analytics.service';

describe('GetAnalyticsService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: GetAnalyticsService = TestBed.get(GetAnalyticsService);
    expect(service).toBeTruthy();
  });
});
