/*
  RESPONSES FROM SERVER
 */

// No constructors

export class NetworkSearchResponse {
  success: boolean;
  totalResult: number;
  content: {
    pdfTitle: string;
    pdfName: string;
    // pdfContent: string;
  }[];
}

export class NetworkPdfUploadResponse {
  success: boolean;
}

export class NetworkGetAllPdfResponse {
  success: boolean;
  pdfs: {

  }
}

/*
  REQUESTS TO SERVER
 *

// No Constructors (it can be ok)

export class NetworkSearchRequest {
  query: string;
}

export class NetworkPdfUploadRequest {
  title: string;
  file: File;

  constructor(title: string, file: File) {
    this.title = title;
    this.file = file;
  }
}
