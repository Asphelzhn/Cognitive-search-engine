export class SearchResponse {
  title: string;
  name: string;
  text: string;
  pic: string;
  sentence: string[];
  keywords: {keyword: string, weight: number}[];


  constructor(title: string, name: string, keywords: {keyword: string, weight: number}[]) {
    this.title = title;
    this.name = name;
    this.text = 'Everything you need to know, SEB 2018!!';
    this.pic = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/QR_with_URL_to_' +
      'article_about_QR-code_%28Swedish%29.svg/1200px-QR_with_URL_to_article_about_QR-code_%28Swedish%29.svg.png';
    this.sentence = [];
    this.keywords = keywords;
  }
}

export class Pdf {
  id: number;
  file: string;
  title: string;
  downloads: number;
  favorites: number;


  constructor(id: number, file: string, title: string, downloads: number, favorites: number) {
    this.id = id;
    this.file = file;
    this.title = title;
    this.downloads = downloads;
    this.favorites = favorites;
  }
}

export class TrendingDocumentsResponse {
    pdfName: string;
    trendScore: number;
    title: string;


  constructor(pdfName: string, trendScore: number, title: string) {
    this.pdfName = pdfName;
    this.trendScore = trendScore;
    this.title = title;
  }
}

