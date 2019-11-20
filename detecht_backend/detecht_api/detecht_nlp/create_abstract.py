import spacy
from spacy.lang.en.stop_words import STOP_WORDS


from heapq import nlargest

"""
Henrik & Oskar

För att kunna köra kör först i terminalen
python -m spacy download en_core_web_sm
"""

stopwords = list(STOP_WORDS)
nlp = spacy.load("en_core_web_sm")


def create_abstract(doc, query):
    query = query.split(" ")
    docx = nlp(doc)

    for word in query:
        if word in stopwords:
            query.remove(word)

    print(query)

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
                    if sent not in sentence_scores.keys():  # and not in query.
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:

                        for key in query:
                            if key in str(sent):
                                sentence_scores[sent] += word_frequencies[word.text.lower()]

                        sentence_scores[sent] += word_frequencies[word.text.lower()] / len(sent)


    sentence_scores

    summarized_sentences = nlargest(4, sentence_scores, key=sentence_scores.get)

    summarized_sentences

    for w in summarized_sentences:
        print(w.text)

