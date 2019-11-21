# encoding: utf-8
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


def words(text): return re.findall(r'\w+', text.lower())


class autocompleteWord():
    def __init__(self, number_of_autocompletes):
        # Creates hash
        word_count = Counter(words(open("big.txt").read()))
        # Makes it a dictionary
        dict_for_trie = dict(word_count)
        # Creates the datastructure and forms it accordning to the number of
        # auto corrects
        self.trie = autocomplete_one_word.Trie()
        self.trie.form_trie(dict_for_trie, number_of_autocompletes)

        # Returns autocompleted suggestions. Returns -1 if it's a full word
        # without suggestions. Returns zero if there are no suggestions
    def autocomplete_one_word_api(self, text):
        suggestions = self.trie.find_word_suggestions(text)
        return suggestions


if __name__ == '__main__':
    t1 = time.clock()
    word_counter = Counter(words(open("big.txt").read()))
    t2 = time.clock()
    dictionary_for_trie = dict(word_counter)
    t3 = time.clock()
    theTrie = autocomplete_one_word.Trie()
    t4 = time.clock()
    theTrie.form_trie(dictionary_for_trie, 5)

    t5 = time.clock()
    h = input("Something to autocomplete: ")
    t6 = time.clock()
    autocomp = theTrie.find_word_suggestions(h)
    t7 = time.clock()
    print(autocomp)
    print()
    print("Hash time: " + str(t2-t1))
    print("Dictionary time: " + str(t3-t2))
    print("Trie create first node time: " + str(t4-t3))
    print("Trie completion time: " + str(t5-t4))
    print("Autocomplete time: " + str(t7-t6))
    print("Size of hash: "+str(sys.getsizeof(word_counter)))
    print("Size of trie: "+str(sys.getsizeof(theTrie)))
