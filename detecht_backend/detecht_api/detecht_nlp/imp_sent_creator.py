import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from detecht_api.detecht_nlp.class_imp_set import ImpSent
from heapq import nlargest
from operator import attrgetter

"""
Henrik & Oscar
"""

stopwords = list(STOP_WORDS)
nlp = spacy.load("en_core_web_sm")


# The sentences are returned in a array where the first sentence is the
# first object in the array
def imp_sent_creator(doc, query, size=4):
    imp_sentences = []

    query = query.split(" ")
    docx = nlp(doc)

    for word in query:
        if word in stopwords:
            query.remove(word)

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
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[
                            word.text.lower()]
                    else:

                        for key in query:
                            if key in str(sent):
                                sentence_scores[sent] += word_frequencies[
                                    word.text.lower()]

                        sentence_scores[sent] += (word_frequencies
                                                  [word.text.lower()]
                                                  / len(sent))

    summarized_sentences = nlargest(size, sentence_scores,
                                    key=sentence_scores.get)

    i = 0
    for w in summarized_sentences:
        imp_sentences.append(ImpSent())
        imp_sentences[i].sent = w
        imp_sentences[i].rank = i
        i += 1

    pos = 0
    w = 0
    for sent in sentence_list:

        for rank in imp_sentences:
            if sent == rank.sent:
                rank.order = w
                w += 1
                rank.start_index = (pos)
                rank.end_index = (pos + len(str(rank.sent)))

        pos += len(sent.text) + 1

    imp_sentences.sort(key=attrgetter("order"), reverse=False)
    return imp_sentences
