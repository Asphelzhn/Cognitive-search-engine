# encoding: utf-8
'''
@author: Edward
@file: DateSearch.py
@time: 2019/11/23 10:01
@desc: This is the function for searching document creation date
'''
from detecht_api.detecht_converter.jsonclass import *
from detecht_api.detecht_nlp.weighting_module.WeightingModule import WeightingModule


def get_file(filename):
    f = open(filename + ".json", "r")
    if f.mode == 'r':
        contents = f.read()
    return contents


# The date format is YYYY-MM-DD
def filter_by_date(start_date, end_date, elastic_search_results):
    filter_list = []
    for title in elastic_search_results:
        # open the json file that contain the document information
        json_file = get_file(title)
        json_class_instance = JsonClass(json_file)
        create_time = JsonClass.date_created()
        if (create_time >= start_date and create_time <= end_date):
            filter_list.append(title)
    # return the creation date between start and end date document name list
    return filter_list

# This is the example of using Weighting Module to filter the document in a specific date
if __name__ == '__main__':
    # get the ranked result from Weighting Module
    elastic_search_results = ['Project management', 'python is amazing', 'programming book']
    query = "I like computer"
    sorted_list = WeightingModule.calculate_score_after_weight(elastic_search_results, query)
    print(sorted_list)

    # filter the creation date
    start_date = "2016-05-30"
    end_date = "2019-11-15"
    filter_list = filter_by_date(start_date,sorted_list)
    print(filter_list)