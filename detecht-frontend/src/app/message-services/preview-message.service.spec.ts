import { TestBed } from '@angular/core/testing';

import { PreviewMessageService } from './preview-message.service';

describe('PreviewMessageService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: PreviewMessageService = TestBed.get(PreviewMessageService);
    expect(service).toBeTruthy();
  });
});
