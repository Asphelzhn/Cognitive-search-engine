import time
import re
from collections import Counter

# import spacy
from detecht_api.django_setup import initialize_django
# from detecht_api.detecht_db_handling.keyword import addTotalKeywords
# from detecht_api.models import TotalKeywords
from os import path

initialize_django()
t1 = time.time()


def words(text):
    return re.findall(r'\w+', text.lower())


word_counter = Counter(words(
    open("detecht_api/detecht_nlp/spell_check/big.txt").read()))
if path.exists("temp.txt"):
    word_counter.update(words(open("temp.txt", errors='ignore').read()))

# def uploadTxt(string):
#    t0=time.time()
#    nlp = spacy.load("en_core_web_sm")
#    nlp.max_length= 100000000
#    t1=time.time()
#    doc = nlp(string, disable=["tagger", "parser", "ner"])
#    t2=time.time()
#    for word in doc:
#        addTotalKeywords(word.text.lower())

word_counter = Counter(words(open(
    "detecht_api/detecht_nlp/spell_check/big.txt").read()))


def P(word, N=sum(word_counter.values())):
    """Probability of `word`."""
    p = word_counter[word] / N
    return p


def correction(word):
    """Most probable spelling correction for word."""
    mostProbable = max(candidates(word), key=P)
    return mostProbable


def candidates(word):
    """Generate possible spelling corrections for word."""
    all_possible_spelling_corrections = (known([word])
                                         or known(edits1(word))
                                         or known(edits2(word))
                                         or [word])
    return all_possible_spelling_corrections


def known(words):
    """The subset of `words` that appear in the dictionary of WORDS."""
    real_words = set(w for w in words if w in word_counter)
    return real_words


def edits1(word):
    "All edits that are one edit away from `word`."
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    """All edits that are two edits away from `word`."""
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))
