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
        databaseObject, word_frequencies = imp_sent_creator.imp_sent_creator(text, 80)
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

    def generateAbstract(self,query,impsentenceList):
        # Här skulle jag vilja få in datavasObject samt word frequencies för ett visst dokument
        abstract = imp_sent_creator.generateAbstract(4, impsentenceList)
        print(abstract)

if __name__ == '__main__':
    s=imp_sent_api()

    sentences, word_frequencies = s.upload_find_relevant_sentences(test_imp_sent_creator.document1)
    print(len(sentences))
    print(word_frequencies)
