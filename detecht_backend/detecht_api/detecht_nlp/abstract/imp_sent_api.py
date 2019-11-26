# encoding: utf-8
from detecht_api.detecht_nlp.abstract import imp_sent_creator
import time
import sys
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
        databaseObject= imp_sent_creator.imp_sent_creator(text, 80, 0)
        for(i in databaseObject):
            i

        #Store those variables
    def generateAbstract(self,query,text):
        abstract = imp_sent_creator.imp_sent_creator(text,4, query)
        print(abstract)
