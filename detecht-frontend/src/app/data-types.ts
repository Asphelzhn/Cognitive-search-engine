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

export class Spellcheck {
  word: string;
  spellcheck: string[];


  constructor(word: string, spellcheck: string[]) {
    this.word = word;
    this.spellcheck = spellcheck;
  }
}

export class Abstract {
  sentence: string;
  score: number;
  page: number;

  constructor(sentence: string, score: number, page: number) {
    this.sentence = sentence;
    this.score = score;
    this.page = page;
  }
}


export class SavedDocument {
  title: string;
  pdfName: string;
  keywords: {keyword: string, weight: number}[];
  abstracts: Abstract[];


  constructor(title: string, pdfName: string, keywords: { keyword: string; weight: number }[], abstracts: Abstract[]) {
    this.title = title;
    this.pdfName = pdfName;
    this.keywords = keywords;
    this.abstracts = abstracts;
  }
}

export class AskQuestion {
  keyword: string;
  type: number; // Values: 0 - false, 1 - true, 2 - ask


  constructor(keyword: string, type: number) {
    this.keyword = keyword;
    this.type = type;
  }
}
