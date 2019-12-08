import { Component, OnInit } from '@angular/core';
import {SearchService} from '../../network-services/search.service';
import {AskQuestion, SearchResponse} from '../../data-types';
import {AdminLoginService} from '../../network-services/admin-login.service';

@Component({
  selector: 'app-related-searches-decision-tree',
  templateUrl: './related-searches-decision-tree.component.html',
  styleUrls: ['./related-searches-decision-tree.component.scss']
})
export class RelatedSearchesDecisionTreeComponent implements OnInit {

  askQuestions: AskQuestion[];
  showQuestion: boolean;
  askQuestionId: string;
  question: string;
  query: string;
  userId: number;
  results: SearchResponse[];

  constructor(private searchService: SearchService, private adminLoginService: AdminLoginService) { }

  ngOnInit() {
    this.searchService.searchResponse.subscribe(searchResult => this.results = searchResult);

    this.askQuestionId = '';

    this.searchService.askQuestion.subscribe((askQuestions) => {
      this.askQuestions = askQuestions;
      for (const question of askQuestions) {
        if (question.type === 2) {
          this.showQuestion = true;
          this.question = question.keyword;
        }
      }
    });

    this.searchService.currentSearch.subscribe(query => this.query = query);
    this.adminLoginService.userId.subscribe(userId => this.userId = userId);
  }

  alterView(): void {
    if (this.askQuestionId === '') {
      this.askQuestionId = 'askQuestion';
    } else {
      this.askQuestionId = '';
    }
  }

  alterSearch(yes: boolean): void {
    this.showQuestion = false;

    const newaskQuestions: AskQuestion[] = [];
    for (const askQuestion of this.askQuestions) {
      if (askQuestion.type === 2) {
        if (yes) {
          newaskQuestions.push(new AskQuestion(askQuestion.keyword, 1));
        } else {
          newaskQuestions.push(new AskQuestion(askQuestion.keyword, 0));
        }
      } else {
        newaskQuestions.push(askQuestion);
      }
    }

    this.searchService.search(this.query, this.userId, newaskQuestions)
  }

}
