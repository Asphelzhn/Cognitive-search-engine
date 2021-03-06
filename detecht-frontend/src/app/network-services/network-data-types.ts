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
  askQuestions: AskQuestion[];
}

export class AskQuestion {
  keyword: string;
  type: number;
}

export class NetworkPdfUploadResponse {
  success: boolean;
  abstracts: string[];
}

export class NetworkAbstractResponse {
  success: boolean;
  abstracts: {
    sentence: string;
    score: number;
    page: number;
  }[];
}

export class GetDocResponse {
  success: boolean;
  pdfTitle: string;
  pdfName: string;
  keywords: {keyword: string, weight: number}[];
  abstracts: {
    sentence: string;
    score: number;
    page: number;
  }[];
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

export class NetworkTrendingDocumentsResponse {
  content: [
    {
      pdf_name: string;
      trend_score: number;
      title: string;
    }
    ];
}

export class NetworkRelatedDocumentResponse {
  success: boolean;
  content: [
    {
      pdfName: string;
      value: number;
      title: string;
      liked: boolean;
    }
    ];
}

export class NetworkGetFavoriteDocumentsResponse {
  success: boolean;
  pdfs: [
    {
      title: string;
      pdfName: string;
      keywords: {keyword: string, weight: number}[];
      abstracts: {
        sentence: string;
        score: number;
        page: number;
      }[];
    }
    ];
}

export class NetworkAdminLoginResponse {
  // tslint:disable-next-line:variable-name
  key: string;
  detail: string;
}

export class NetworkGetAnalyticsResponse {
  documents: number;
  downloads: number;
  favorites: number;
}

export class  NetworkIsFavoriteResponse {
  success: boolean;
  favorite: boolean;
}

export class NetworkSuccessResponse {
  success: boolean;
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

export class NetworkTrendingDocumentsRequest {
  size: number;
}

export class NetworkInteractWithDocumentRequest {
  pdfName: string;
  userId: number;
  type: string;


  constructor(pdfName: string, userId: number, type: string) {
    this.pdfName = pdfName;
    this.userId = userId;
    this.type = type;
  }
}

export class NetworkFavoriteDocumentRequest {
  userId: number;
  pdfName: string;
  like: boolean;


  constructor(userId: number, pdfName: string, like: boolean) {
    this.userId = userId;
    this.pdfName = pdfName;
    this.like = like;
  }
}

export class NetworkRelatedDocumentRequest {
  name: string;
}

export class NetworkAdminLoginRequest {
  username: string;
  // email: string;
  password: string;
}

export class NetworkChangeNameRequest {
  pdfName: string;
  newTitle: string;
}
