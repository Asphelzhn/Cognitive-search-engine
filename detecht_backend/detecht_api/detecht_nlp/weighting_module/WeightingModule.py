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


class WeightingModule:

    def __init__(self):
        global nlp = spacy.load('en_core_web_sm')

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
                index +=1


    def calculate_keyword_similarity(self, elastic_search_results, search_query):
        similarity_list = []

        # Todo fix
        for title in elastic_search_results:
            title_no_stop = nlp(''.join(([str(t) for t in title if not t.is_stop])))
            search_query_no_stop = nlp(''.join(([str(t) for t in search_query if not t.is_stop])))
            similarity = title_no_stop.similarity(search_query_no_stop)
            similarity_list.append(similarity)

        return similarity_list

    def normalize(self, temp, min, max):
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
        similarity_list = WeightingModule.calculate_keyword_similarity(elastic_search_results, search_query)
        index = 0
        for result in elastic_search_results:
            score_dict[result] += weight_keyword_similarity * similarity_list[index]
            index += 1

        # add popularity to weight

        return sorted_list
