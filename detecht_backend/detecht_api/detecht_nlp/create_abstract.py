import spacy
from spacy.lang.en.stop_words import STOP_WORDS

from heapq import nlargest
from collections import Counter

"""
Henrik & Oskar

För att kunna köra kör först i terminalen
python -m spacy download en_core_web_sm
"""

stopwords = list(STOP_WORDS)
nlp = spacy.load("en_core_web_sm")
hashForSpeed = Counter()


def create_hash(doc):
    docx = nlp(doc)
    i = 0
    j = 0
    for word in docx:
        if word.text not in stopwords:
            hashForSpeed[word.text] = hashForSpeed[word.text] + 1


def create_abstract(query, doc):
    docx = nlp(doc)
    query = nlp(query)
    queryList = []
    for word in query:
        if word.text.lower() not in stopwords:
            queryList.append(word.text.lower)

    # print(query)

    #  maximum_frequency = max(word_frequencies.values())

    #  for word in word_frequencies.keys():
    #    word_frequencies[word] = (word_frequencies[word] / maximum_frequency)

    sentence_list = [sentence for sentence in docx.sents]

    sentence_scores = Counter()
    for sent in sentence_list:
        if len(sent.text.split(' ')) < 30:
            for word in sent:
                if word.text not in stopwords:
                    if sentence_scores[sent.text] == 0:  # and not in query.
                        sentence_scores[sent.text] = \
                            hashForSpeed[word.text.lower()] / len(sent)
                    else:
                        sentence_scores[sent.text] += \
                            hashForSpeed[word.text.lower()] / len(sent)
                    for key in queryList:
                        if key in sent.text.lower().split(' '):
                            sentence_scores[sent.text] += \
                                hashForSpeed[word.text.lower()] / len(sent)
                        #     print (sentence_scores[sent])
                        #      print(key + "  key word found")
                    # print(len(sent))
                    # print (sent)

    summarized_sentences = nlargest(4, sentence_scores,
                                    key=sentence_scores.get)

    final_sentences = [w for w in summarized_sentences]

    summary = ' '.join(final_sentences)

    # print(len(summary))
    # print(summary)

    # print(len(summary))
    # len(document1)

    return summary
