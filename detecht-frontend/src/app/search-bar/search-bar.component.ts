import {Component, Input, OnInit} from '@angular/core';
import {Router} from '@angular/router';
import {SearchService} from '../network-services/search.service';
import {SearchResponse, Spellcheck} from '../data-types';
import {NetworkAutoCompleteResponse, NetworkSearchResponse} from '../network-services/network-data-types';
import {AdminLoginService} from '../network-services/admin-login.service';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.scss']
})
export class SearchBarComponent implements OnInit {

  constructor(private searchService: SearchService, private router: Router, private adminLoginService: AdminLoginService) { }

  searchString: string;
  spellcheck: Spellcheck[];
  showSpellcheck: boolean;
  showSpellcheckDropDown: boolean;
  spellcheckDropDown: Spellcheck;
  autocomplete: string[];
  userId: number;
  @Input() changePage: boolean;

  ngOnInit() {
    this.adminLoginService.userId.subscribe(userId => this.userId = userId );

    this.searchService.currentSearch.subscribe(query => this.searchString = query);
    this.searchService.spellcheck.subscribe((spellcheck) => {
      this.spellcheck = spellcheck;
      if (spellcheck.length > 0) {
        this.showSpellcheck = false;
        for (const spellcheckWord of spellcheck) {
          if (!spellcheckWord.spellcheck.includes(spellcheckWord.word.toLowerCase()) && !spellcheckWord.spellcheck.includes(spellcheckWord.word)) {
            this.showSpellcheck = true;
          }
        }
      } else {
        this.showSpellcheck = false;
      }
    });
    this.showSpellcheckDropDown = false;
    this.spellcheckDropDown = {word: '', spellcheck: []};
    this.autocomplete = [];
  }

  spellcheckClass(spellcheckWord: Spellcheck): string {
    if (spellcheckWord.spellcheck.includes(spellcheckWord.word.toLowerCase()) && !spellcheckWord.spellcheck.includes(spellcheckWord.word)) {
      return '';
    } else {
      return 'misspelled';
    }
  }

  pressedSpellcheck(spellcheckWord: Spellcheck) {
    if (spellcheckWord === undefined) {
      this.showSpellcheck = false;
    } else {
      if (spellcheckWord.spellcheck.includes(spellcheckWord.word.toLowerCase()) && !spellcheckWord.spellcheck.includes(spellcheckWord.word)) {
        this.showSpellcheck = false;
      } else {
        this.showSpellcheckDropDown = true;
        this.spellcheckDropDown = spellcheckWord;
      }
    }
  }

  closeSpellcheckDropDown() {
    this.showSpellcheckDropDown = false;
  }

  closeAutocompleteDropDown() {
    this.autocomplete = [];
  }

  updateAutoComplete() {
    if (this.searchString === '') {
      this.autocomplete = [];
    } else {
      this.searchService.autocomplete(this.searchString).subscribe(
        (data: NetworkAutoCompleteResponse) => {
          console.log('AutoComplete: ');
          console.log(data);
          if (data.success) {
            this.autocomplete = data.autocomplete;
          } else {
            console.log('Error when getting schedule, please refresh the results');
          }
        },
        (error: any) => {
          console.log(error);
        }
      );
    }
  }

  autoComplete(sentence: string) {
    this.autocomplete = [];
    this.searchString = sentence;
    this.search();
  }

  search(): void {
    console.log('Searching for: ' + this.searchString);
    this.autocomplete = [];
    this.searchService.search(this.searchString, this.userId);
    if (this.changePage) {
      this.router.navigateByUrl('search');
    }
  }

  searchForSpellcheck(word: string, newWord: string) {
    this.closeSpellcheckDropDown();
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
    this.searchService.search(newQuery, this.userId);
  }

}
