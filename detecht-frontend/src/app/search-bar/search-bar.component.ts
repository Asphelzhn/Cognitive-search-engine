import {Component, Input, OnInit} from '@angular/core';
import {Router} from '@angular/router';
import {SearchService} from '../network-services/search.service';
import {Spellcheck} from '../data-types';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.scss']
})
export class SearchBarComponent implements OnInit {

  constructor(private searchService: SearchService, private router: Router) { }

  searchString: string;
  spellcheck: Spellcheck[];
  showSpellcheck: boolean;
  showSpellcheckDropDown: boolean;
  spellcheckDropDown: Spellcheck;
  @Input() changePage: boolean;

  ngOnInit() {
    this.searchService.currentSearch.subscribe(query => this.searchString = query);
    this.searchService.spellcheck.subscribe((spellcheck) => {
      this.spellcheck = spellcheck;
      if (spellcheck.length > 0) {
        this.showSpellcheck = false;
        for (const spellcheckWord of spellcheck) {
          if (!spellcheckWord.spellcheck.includes(spellcheckWord.word)) {
            this.showSpellcheck = true;
          }
        }
      } else {
        this.showSpellcheck = false;
      }
    });
    this.showSpellcheckDropDown = false;
    this.spellcheckDropDown = {word: '', spellcheck: []};
  }

  spellcheckClass(spellcheckWord: Spellcheck): string {
    if (spellcheckWord.spellcheck.includes(spellcheckWord.word)) {
      return '';
    } else {
      return 'misspelled';
    }
  }

  pressedSpellcheck(spellcheckWord: Spellcheck) {
    if (spellcheckWord === undefined) {
      this.showSpellcheck = false;
    } else {
      if (spellcheckWord.spellcheck.includes(spellcheckWord.word)) {
        this.showSpellcheck = false;
      } else {
        this.showSpellcheckDropDown = true;
        this.spellcheckDropDown = spellcheckWord;
      }
    }
  }

  closeDropDown() {
    this.showSpellcheckDropDown = false;
  }

  search(): void {
    console.log('Searching for: ' + this.searchString);
    this.searchService.search(this.searchString);
    if (this.changePage) {
      this.router.navigateByUrl('search');
    }
  }

  searchForSpellcheck(word: string, newWord: string) {
    this.closeDropDown();
    console.log('Word: ' + word + ' NewWord: ' + newWord);
    let newQuery = '';
    for (const queryWord of this.spellcheck) {
      if (queryWord.word === word) {
        newQuery += newWord;
      } else {
        newQuery += queryWord.word;
      }
      newQuery += ' ';
    }
    console.log('NewQuery:' + newQuery);
    this.searchService.search(newQuery);
  }

}
