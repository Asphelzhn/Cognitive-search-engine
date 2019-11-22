import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'detecht_backend.settings'
import django

django.setup()
from detecht_api.models import Search_Autocomplete
'''
By Severn
'''

def get_autocomplete(query):
    # search database, get all the n_gram start with query
    result = Search_Autocomplete.objects.filter(n_gram__istartswith=query)
    # return 0 if no result
    if result.count() == 0:
        return 0
    # put n_gram into a list
    gram_list = []
    for r in result:
        gram_list.append(r.n_gram)
    n2gram = []
    n3gram = []
    n4gram = []
    n5gram = []
    for g in gram_list:
        if len(g.split()) == 2:
            n2gram.append(g)
        if len(g.split()) == 3:
            n3gram.append(g)
        if len(g.split()) == 4:
            n4gram.append(g)
        if len(g.split()) == 5:
            n5gram.append(g)
    # Return different results depending on the length of the query
    query_len = len(query.split())
    result_list = []
    if query_len == 1:
        result_list = n2gram[:4] + n3gram[:3]
    if query_len == 2:
        result_list = n3gram[:4] + n4gram[:2] + n5gram[:1]
    if query_len == 3:
        result_list = n4gram[:3] + n5gram[:2]
    if query_len == 4:
        result_list = n5gram[:3]
    return result_list


def test():
    print(get_autocomplete("In the"))
