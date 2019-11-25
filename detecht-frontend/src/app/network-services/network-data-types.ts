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
    keywords: {keyword: string, weight: number}[];
    // pdfContent: string;
  }[];
  spellcheck: {word: string, spellcheck: string[]}[];
}

export class NetworkPdfUploadResponse {
  success: boolean;
  abstracts: string[];
}

export class NetworkAbstractResponse {
  success: boolean;
  abstracts: {sentence: string}[];
}

export class NetworkAutoCompleteResponse {
  success: boolean;
  autocomplete: string[];
}

export class NetworkGetAllPdfResponse {
  data: [
    {
      id: number;
      file: string;
      title: string;
      downloads: number;
      favorites: number;
    }
    ];
}

/*
  REQUESTS TO SERVER
 */

// No Constructors (it can be ok)

export class NetworkSearchRequest {
  query: string;
}

export class NetworkAbstractRequest {
  query: string;
  pdf: string;

  constructor(query: string, pdf: string) {
    this.query = query;
    this.pdf = pdf;
  }
}

export class NetworkPdfUploadRequest {
  title: string;
  file: File;

  constructor(title: string, file: File) {
    this.title = title;
    this.file = file;
  }
}
