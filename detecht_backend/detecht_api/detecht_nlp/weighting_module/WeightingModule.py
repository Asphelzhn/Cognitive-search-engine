# encoding: utf-8
'''
@author: Edward & Severn
@file: WeightingModule.py
@time: 2019/11/12 22:05
@desc: This is the class for weighting module.
This module receives the list of search results from Elastic Search, calculate a weight for each based on a set of factors, sort the list, and return that sorted list.
The "set of factors" that influence the weight of a document are preliminarily:
ES-Score（Elastic Search results）
Keyword similarity (compilation of the weight of matched keywords)
Popularity (#downloads & #favorites)
'''
import spacy

from detecht_api import models

nlp = spacy.load('en_core_web_sm')


class WeightingModule:

    # def __init__(self):
    #     global nlp = spacy.load('en_core_web_sm')

    def get_factors(self, elastic_search_results, keyword_similarity, popularity):
        pass

    # downloads should be [(elastic_search_result，downloads)]
    # favourite should be [user_keyword1, user_keyword2]
    def calculate_popularity(self, downloads, favourites, elastic_search_results):
        weight_downloads = 2
        weight_favourite = 8

        popularity_score = []
        index = 0
        for title in elastic_search_results:
            for user_keyword in favourites:
                title_no_stop = nlp(''.join(([str(t) for t in title if not t.is_stop])))
                favourite_similarity = user_keyword.similarity(title_no_stop)
                popularity_score[index] += favourite_similarity
                index += 1

    # calculate the similarity between search_query and each document keyword
    def calculate_keyword_similarity(self, elastic_search_results, search_query):
        similarity_list = []
        search_query_no_stop = nlp(''.join(([str(t) for t in search_query if not t.is_stop])))

        for title in elastic_search_results:
            # get document keywords in database
            name_weight_set = models.Pdf_Name_Keyword_Weight.objects.filter(pdf_name=title)
            score_after_weight = 0
            for name in name_weight_set:
                keyword = name.keyword
                keyword_weight = name.weight

                # print(keyword)
                # print(keyword)

                similarity = (keyword.similarity(search_query_no_stop)) * keyword_weight
                score_after_weight += similarity

            similarity_list.append(score_after_weight)

        return similarity_list

    def normalize(temp, min, max):
        return (temp - min) / (max - min)

    def calculate_weight(self, elastic_search_results, search_query):
        score_dict = {}
        length = len(elastic_search_results)

        # weight of each factors
        weight_elastic_search = 5
        weight_keyword_similarity = 4
        weight_popularity = 1

        # initial weight of elastic_search_results
        for result in elastic_search_results:
            initial_score = WeightingModule.normalize(length, 0, len(elastic_search_results))
            score_dict[result] = weight_elastic_search * initial_score
            length -= 1

        # add keyword similarity to weight
        similarity_score_list = WeightingModule.calculate_keyword_similarity(elastic_search_results, search_query)
        max_score = max(similarity_score_list)
        min_score = min(similarity_score_list)
        normalize_similarity_score_list = []
        for i in range(0, len(similarity_score_list)):
            normalize_similarity_score_list[i] = WeightingModule.normalize(similarity_score_list[i], min_score,
                                                                           max_score)

        index = 0
        for result in elastic_search_results:
            score_after_keyword_weight = weight_keyword_similarity * normalize_similarity_score_list[index]

            score_dict[result] += score_after_keyword_weight
            index += 1

        # add popularity to weight



        # return sorted_list


# This is the example how to use Weighting Module to add return a new sorted list.
if __name__ == '__main__':
    name_weight_set = models.Pdf_Name_Keyword_Weight.objects.filter(pdf_name="document1")
    for name in name_weight_set:
        keyword = name.keyword
        print(keyword)
