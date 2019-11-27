import { TestBed } from '@angular/core/testing';

import { UserFavoriteService } from './user-favorite.service';

describe('UserFavoriteService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: UserFavoriteService = TestBed.get(UserFavoriteService);
    expect(service).toBeTruthy();
  });
});
