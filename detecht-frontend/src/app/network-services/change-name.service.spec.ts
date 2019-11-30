import { TestBed } from '@angular/core/testing';

import { ChangeNameService } from './change-name.service';

describe('ChangeNameService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ChangeNameService = TestBed.get(ChangeNameService);
    expect(service).toBeTruthy();
  });
});
