export class SearchResponse {
  title: string;
  name: string;
  text: string;
  pic: string;


  constructor(title: string, name: string, text: string, pic: string) {
    this.title = title;
    this.name = name;
    this.text = 'Everything you need to know, SEB 2018!!';
    this.pic = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/QR_with_URL_to_' +
      'article_about_QR-code_%28Swedish%29.svg/1200px-QR_with_URL_to_article_about_QR-code_%28Swedish%29.svg.png';
  }
}

