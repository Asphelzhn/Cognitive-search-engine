import datetime

from detecht_api import models
import spacy
"""
get the popular search during a time
Edward and Severn
"""

nlp = spacy.load("en_core_web_sm")


def word_frequency(query):
    # put all the words of standardized_search_query into one list
    words = []
    query = models.Searches_Database.objects.all().values_list("standardized_search_query")
    print(query)
    for row in query:
        temp = row[0]
        # print(temp)
        # print(type(temp))
        temp = temp.replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
        # print(temp)
        list = temp.split(",")
        for word in list:
            words.append(nlp(word))
        # print(list)
        break
    '''
    words = []
    for s_query in query:
        test_doc = nlp(s_query.standardized_search_query)
        for i in test_doc:
            words.append(i)
    # print(words)
    '''
    tf = {}
    # Word frequency statistics
    for word in words:
        word = word.lower()
        # word = ''.join(word.split())
        if word in tf:
            tf[word] += 1
        else:
            tf[word] = 1
    # return a dictionary with sorted word frequency
    key_value_pairs = sorted([(tz, count) for tz, count in tf.items()], reverse=True)

    for word in key_value_pairs[0:10]:
        print("{0:10}{1}".format(word[1], word[0]))
    return key_value_pairs


# Get popular searches
def get_popular_search():
    query = models.Searches_Database.objects.all().values()
    return word_frequency(query)


# Get popular searches during a timeframe
# the format of date must be "Year-Month-Day" and date1 < date2
def get_period_popular_search(date1, date2):
    if date1 > date2:
        return "Wrong input"
    query = models.Searches_Database.objects.period_date(field='search_date', start_time=date1, end_time=date2)
    return word_frequency(query)


# this is example of how to get popular search during a time
if __name__ == '__main__':
    words = []
    query = models.Searches_Database.objects.all().values_list("standardized_search_query")
    print(query)
    for row in query:
        temp = row[0]
        print(temp)
        print(type(temp))
        temp = temp.replace("[", "").replace("]","").replace("'","").replace(" ","")
        print(temp)
        list = temp.split(",")
        for word in list:
            words.append(nlp(word))
    print(words)



    # popular = get_popular_search()
    # print(popular)
    #
    # # specify a time
    # now = datetime.now()
    # end_date = datetime.strftime("%Y-%m-%d %H:%M:%S.%f", now)
    # # get ten days earlier
    # start_date = datetime.strftime("%Y-%m-%d %H:%M:%S.%f",now - datetime.timedelta(days= 10))
    # popular_in_time = get_period_popular_search(start_date,end_date)
    # print(popular_in_time)