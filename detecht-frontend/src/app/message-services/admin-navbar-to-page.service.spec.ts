import { TestBed } from '@angular/core/testing';

import { AdminNavbarToPageService } from './admin-navbar-to-page.service';

describe('AdminNavbarToPageService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: AdminNavbarToPageService = TestBed.get(AdminNavbarToPageService);
    expect(service).toBeTruthy();
  });
});
