from datetime import datetime, timedelta

from detecht_api import models
import spacy
"""
get the popular search during a time
Edward and Severn
"""

nlp = spacy.load("en_core_web_sm")


# end_date could be none, which mean till now
def word_frequency(start_date, end_date=datetime.now()):
    if(start_date is not None):
        search_start_date = start_date
        search_end_date = end_date
        search_filter = models.Searches_Database.objects.filter(search_date__range=(search_start_date, search_end_date))
        query = search_filter.values_list("standardized_search_query")
    else:
        query = models.Searches_Database.objects.all().values_list("standardized_search_query")

    # put all the words of standardized_search_query into one list
    words = []
    # print(query)
    for row in query:
        temp = row[0]
        # print(temp)
        # print(type(temp))
        temp = temp.replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
        # print(temp)
        list = temp.split(",")
        for word in list:
            words.append(word)
        # print(list)
    # Word frequency statistics
    word_frequency_dict = {}
    for word in words:
        word = word.lower()
        if word in word_frequency_dict.keys():
            word_frequency_dict[word] += 1
        else:
            word_frequency_dict[word] = 1
    # print(word_frequency_dict)
    # return a dictionary with sorted word frequency
    sorted_word_frequency_dict = sorted(word_frequency_dict.items(), key=lambda item: item[1], reverse=True)

    return sorted_word_frequency_dict


# Get popular searches
def get_popular_search():
    # query = models.Searches_Database.objects.all().values()
    return word_frequency(None)


# Get popular searches during a timeframe
# the format of date must be "Year-Month-Day" and date1 < date2
def get_period_popular_search(date1, date2):
    if date1 > date2:
        return "Wrong input"
    return word_frequency(date1, date2)


# this is example of how to get popular search during a time
if __name__ == '__main__':

    popular = get_popular_search()
    print("popular search:")
    print(popular)

    # specify a time
    end_date = datetime.now()
    # get ten days earlier
    start_date = end_date - timedelta(days=10)
    popular_in_time = get_period_popular_search(start_date, end_date)
    print("#"*30)
    print("poplular search in a time:")
    print(popular_in_time)
