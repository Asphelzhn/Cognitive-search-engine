import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from detecht_api.detecht_nlp.abstract.class_imp_set import *
from heapq import nlargest
from operator import attrgetter
import time

"""
Henrik & Oscar
"""

stopwords = list(STOP_WORDS)
nlp = spacy.load("en_core_web_sm")


# The sentences are returned in a array where the first sentence is the first object in the array

#def relevantSentenceAbstract(doc,size):
#    sentences= imp_sent_creator(doc,80,0)
#    for i in sentences:



def imp_sent_creator(doc, size):
    imp_sentences = []
    docx = nlp(doc)
    word_frequencies = {}

    for word in docx:
        if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1

    maximum_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word] / maximum_frequency)

    sentence_list = [sentence for sentence in docx.sents]

    sentence_scores = {}
    for sent in sentence_list:
        if len(sent.text.split(' ')) < 30:
            for word in sent:
                if word.text.lower() in word_frequencies.keys():
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]/len(sent)
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]/len(sent)
                    #if query!= 0:
                    #    for key in query:
                    #        if key in str(sent):
                    #            sentence_scores[sent] += word_frequencies[word.text.lower()]/len(sent)


    summarized_sentences = nlargest(size, sentence_scores, key=sentence_scores.get)

    i = 0
    for w in summarized_sentences:
        imp_sentences.append(ImpSent())
        imp_sentences[i].sent = w
        imp_sentences[i].rank = i
        imp_sentences[i].score = sentence_scores[w]
        i += 1

    pos = 0
    w = 0
    for sent in sentence_list:
        for i in imp_sentences:
            if sent == i.sent:
                i.order = w
                w += 1
                i.start_index = (pos)
                i.end_index = (pos + len(str(i.sent)))

        pos += len(sent.text) + 1

    imp_sentences.sort(key=attrgetter("order"), reverse=False)

    return imp_sentences, word_frequencies

def generateAbstract(query,impSentenceList,word_frequencies,size):
    copiedImpSent=[]
    query = query.split(" ")

    for word in query:
        if word in stopwords:
            query.remove(word)

    sentence_scores = {}
    for i in impSentenceList:
        sentence_scores[i.sent]=i.score.copy()
        for word in i.sent:
            #Behöver databas
            if word.text.lower() in word_frequencies.keys():
                    for key in query:
                        if key in str(i.sent):
                            sentence_scores[i.sent] += word_frequencies[word.text.lower()]/len(i.sent)

    summarized_sentences = nlargest(size, sentence_scores, key=sentence_scores.get)

    i = 0
    for w in summarized_sentences:
        copiedImpSent.append(ImpSent())
        copiedImpSent[i].sent = w
        copiedImpSent[i].rank = i
        copiedImpSent[i].score = sentence_scores[w]
        i += 1

    for x in impSentenceList:
        for i in copiedImpSent:
            if i.sent == x.sent:
                i.order = x.order.copy()
                i.start_index = x.start_index.copy()
                i.end_index = (i.start_index + len(str(i.sent)))

    copiedImpSent.sort(key=attrgetter("order"), reverse=False)

    return copiedImpSent

