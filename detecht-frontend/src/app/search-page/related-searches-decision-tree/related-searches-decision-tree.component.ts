import { Component, OnInit } from '@angular/core';
import {SearchService} from '../../network-services/search.service';
import {AskQuestion} from '../../data-types';

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

  constructor(private searchService: SearchService) { }

  ngOnInit() {

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
  }

  alterView(): void {
    if (this.askQuestionId === '') {
      this.askQuestionId = 'askQuestion';
    } else {
      this.askQuestionId = '';
    }
  }

}
