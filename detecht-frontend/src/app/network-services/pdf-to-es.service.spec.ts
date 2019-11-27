import { TestBed } from '@angular/core/testing';

import { PdfToEsService } from './pdf-to-es.service';

describe('PdfToEsService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: PdfToEsService = TestBed.get(PdfToEsService);
    expect(service).toBeTruthy();
  });
});
