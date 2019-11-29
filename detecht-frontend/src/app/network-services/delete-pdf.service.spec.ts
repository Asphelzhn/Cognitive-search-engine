import { TestBed } from '@angular/core/testing';

import { DeletePdfService } from './delete-pdf.service';

describe('DeletePdfService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: DeletePdfService = TestBed.get(DeletePdfService);
    expect(service).toBeTruthy();
  });
});
