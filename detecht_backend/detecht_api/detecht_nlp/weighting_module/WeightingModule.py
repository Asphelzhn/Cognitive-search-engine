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
from detecht_api.detecht_db_handling.analytics import get_analytics_document

nlp = spacy.load('en_core_web_sm')


class WeightingModule:

    # def __init__(self):
    #     global nlp = spacy.load('en_core_web_sm')



    def get_factors(elastic_search_results, keyword_similarity, popularity):
        pass

    # calculate the similarity between search_query and each document keyword
    def calculate_keyword_similarity(elastic_search_results, search_query, user_keywords = []):
        similarity_list = []
        search_query = nlp(search_query)
        search_query_no_stop = nlp(''.join(([str(t) for t in search_query if not t.is_stop])))

        for pdfname in elastic_search_results:
            # get document keywords in database
            name_weight_set = models.Pdf_Name_Keyword_Weight.objects.filter(pdf_name=pdfname)
            score_after_weight = 0
            for doc in name_weight_set:
                keyword = nlp(doc.keyword)
                keyword_weight = doc.weight

                similarity = (keyword.similarity(search_query_no_stop)) * keyword_weight
                score_after_weight += similarity
                if doc.keyword in user_keywords:
                    score_after_weight += 1

            similarity_list.append(score_after_weight)

        return similarity_list

    def calculate_popularity(elastic_search_results):
        popularity_score = []

        download_weight = 4
        favourite_weight = 6
        for pdfname in elastic_search_results:
            record = models.Document.objects.get(file='detecht_api/static/pdf/' + pdfname)
            download = record.downloads
            favourite = record.favorites
            score = download * download_weight + favourite * favourite_weight
            popularity_score.append(score)


        max_score = max(popularity_score)
        min_score = min(popularity_score)
        normalize_popularity_score = []
        for popularity in popularity_score:
            normalize_popularity_score.append(WeightingModule.normalize(popularity, min_score, max_score))
        return normalize_popularity_score

    def normalize(temp, min, max):
        minus_result = max - min
        if(minus_result == 0):
            minus_result = 1000000

        return (temp - min) / minus_result

    def calculate_score_after_weight(elastic_search_results, search_query, user_id = -1):
        user_keywords = []
        if user_id != -1:
            user_keywords_result = models.User_Keyword.objects.filter(userID=user_id)
            for user_keyword in user_keywords_result:
                user_keywords.append(user_keyword.keyword)

        score_dict = {}
        length = len(elastic_search_results)

        # weight of each factors
        weight_elastic_search = 0.470591667
        weight_keyword_similarity = 0.449807667
        weight_popularity = 0.079600333

        # initial weight of elastic_search_results
        for result in elastic_search_results:
            initial_score = WeightingModule.normalize(length, 0, len(elastic_search_results))
            score_dict[result] = weight_elastic_search * initial_score
            length -= 1

        # add keyword similarity to weight
        similarity_score_list = WeightingModule.calculate_keyword_similarity(elastic_search_results, search_query, user_keywords)
        max_score = max(similarity_score_list)
        min_score = min(similarity_score_list)
        normalize_similarity_score_list = []
        for similarity in similarity_score_list:
            normalize_similarity_score_list.append(WeightingModule.normalize(similarity, min_score, max_score))

        index = 0
        for result in elastic_search_results:
            score_after_keyword_weight = weight_keyword_similarity * normalize_similarity_score_list[index]

            score_dict[result] += score_after_keyword_weight
            index += 1

        # add popularity to weight

        popularity_score_list = WeightingModule.calculate_popularity(elastic_search_results)
        index = 0
        for result in elastic_search_results:
            score_after_popularity_weight = weight_popularity * popularity_score_list[index]

            score_dict[result] += score_after_popularity_weight
            index += 1

        sorted_document_list = sorted(score_dict.items(), key=lambda item: item[1], reverse=True)

        result_list = []
        for element in sorted_document_list:
            result_list.append(element[0])
        return result_list

    # This function is used for ask me a question, return the most frequent keyword and document list that include it
    def ask_a_question(ranked_by_weighting_module_results):
        keywords_dict = {}
        for pdfname in ranked_by_weighting_module_results:
            # get document keywords in database
            name_weight_set = models.Pdf_Name_Keyword_Weight.objects.filter(pdf_name=pdfname)
            # print("query result")
            # print(name_weight_set)
            for name in name_weight_set:
                keyword = name.keyword
                # print(keyword)
                if keyword in keywords_dict.keys():
                    keywords_dict[keyword] += 1
                else:
                    keywords_dict[keyword] = 1
        # print("dict is")
        # print(keywords_dict)
        sorted_keywords_list = sorted(keywords_dict.items(),key=lambda t:t[1], reverse=True)
        occur_most_keyword = sorted_keywords_list[0][0]
        # print(sorted_keywords_list)
        # print(occur_most_keyword)

        prune_result_list =[]
        for title in ranked_by_weighting_module_results:
            # get document keywords in database
            name_weight_set = models.Pdf_Name_Keyword_Weight.objects.filter(pdf_name=title)
            for name in name_weight_set:
                keyword = name.keyword
                pdf_name = name.pdf_name
                if(keyword == occur_most_keyword):
                    prune_result_list.append(pdf_name)
                    break
        return occur_most_keyword,prune_result_list



if __name__ == '__main__':
    # This is the example how to use Weighting Module to add return a new sorted list.

    elastic_search_results = ['Project_management.pdf', 'python_is_amazing.pdf', 'programming_book.pdf']
    query = "I like computer"

    sorted_list = WeightingModule.calculate_score_after_weight(elastic_search_results, query)

    print(sorted_list)

    # This is used for test ask me a question function
    keyword,prune_list = WeightingModule.ask_a_question(sorted_list)
    print(keyword)
    print(prune_list)