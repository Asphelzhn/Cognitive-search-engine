# encoding: utf-8
'''
@author: Edward
@file: DateSearch.py
@time: 2019/11/23 10:01
@desc: This is the function for searching document creation date
'''
from detecht_api.detecht_nlp.weighting_module.WeightingModule import WeightingModule


def filter_by_date(start_date,end_date,elastic_search_results):

    WeightingModule.calculate_score_after_weight(elastic_search_results, search_query)

# This is the example of using Weighting Module to filter the document in a specific date
if __name__ == '__main__':
    elastic_search_results = ['Project management', 'python is amazing', 'programming book']
    query = "I like computer"

    sorted_list = WeightingModule.calculate_score_after_weight(elastic_search_results, query)

    print(sorted_list)