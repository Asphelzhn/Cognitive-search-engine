/*
  RESPONSES FROM SERVER
 */

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

/*
  REQUESTS TO SERVER
 */

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
