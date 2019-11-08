from detecht_api.detecht_nlp.autocompleOneWord import autocomplete_one_word
import time
import re
from collections import Counter
import sys


def words(text): return re.findall(r'\w+', text.lower())


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
