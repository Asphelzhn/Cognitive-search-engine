import os
import django
import operator
import time
from detecht_api.models import Search_Autocomplete
from detecht_api.detecht_nlp.autocompleteWords import n_gram

os.environ['DJANGO_SETTINGS_MODULE'] = 'detecht_backend.settings'
django.setup()

'''
By Severn
'''


def upload():
    t1 = time.clock()
    content = open("detecht_api/detecht_nlp/autocompleteWords/big.txt").read()
    n_grams = n_gram.getNgrams(content, 6)
    sortedNGrams = sorted(n_grams.items(), key=operator.itemgetter(1),
                          reverse=True)  # =True descending sort
    t2 = time.clock()
    print("Data processing time: " + str(t2 - t1))
    # delete old data in  the database
    Search_Autocomplete.objects.all().delete()
    # write data in to database
    work_list = []
    for s in sortedNGrams:
        if s[1] > 1:
            work_list.append(Search_Autocomplete(n_gram=str(s[0]),
                                                 frequency=int(s[1])))
    Search_Autocomplete.objects.bulk_create(work_list)
    t3 = time.clock()
    print("Data upload time: " + str(t3 - t2))
    print("uploaded")
