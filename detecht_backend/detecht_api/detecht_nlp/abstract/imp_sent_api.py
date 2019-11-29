# encoding: utf-8
from detecht_api.detecht_nlp.abstract import imp_sent_creator
import time
import sys
from detecht_api.detecht_nlp.abstract import test_imp_sent_creator

'''
@author: Samuel
@file: autocomplete_one_word_api.py
@time: 2019/11/12 21:01
@desc: This is using a trie to implement autocomplete for one word
'''
from detecht_api.detecht_nlp.autocompleOneWord import autocomplete_one_word
import time
import re
from collections import Counter
import sys

class imp_sent_api():
    def upload_find_relevant_sentences(self, text):
        size=80
        databaseObject, word_frequencies = imp_sent_creator.imp_sent_creator(text, 40)
        #Allt som returneras ska in i databasen för varje dokument
        #DatabaseObject är en lista av 80st ImpSent med följande info:
        #class ImpSent:
        #    sent = str
        #    rank = int
        #    order = int
        #    start_index = int
        #    end_index = int
        #    score = float
        # word frequencies en dictionary med ord samt float viketer
        return databaseObject, word_frequencies

    def generateAbstract(self,query,impsentenceList,word_frequencies):
        # Här skulle jag vilja få in datavasObject samt word frequencies för ett visst dokument
        size=4
        abstract = imp_sent_creator.generateAbstract(query, impsentenceList, size, word_frequencies)
        return abstract

if __name__ == '__main__':
    s=imp_sent_api()

    sentences, word_frequencies = s.upload_find_relevant_sentences([test_imp_sent_creator.document1])
    t0=time.time()
    a = s.generateAbstract("Shelock Holmes", sentences, word_frequencies)
    t1= time.time()
    print(t1-t0)
    for i in a:
        print("Sentence: " + str(i.sent))
        print("Start index: " + str(i.start_index))
        print("End index: " + str(i.end_index))
        print("Score: " + str(i.score))
        print("Order: "+ str(i.order))
        print("Rank: "+ str(i.rank))
        print("Page: " + str(i.page))



