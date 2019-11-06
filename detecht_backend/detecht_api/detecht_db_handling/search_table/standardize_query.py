import spacy
from spacy.lang.en.stop_words import STOP_WORDS
"""
standardized_search_query
Edward & Severn
"""

nlp = spacy.load("en_core_web_sm")
stopwords = list(STOP_WORDS)

def standardize_query(query):
    my_doc = nlp(query)

    # could add customize stop words here
    customize_stop_words = [
        'computing', 'filtered'
    ]
    for w in customize_stop_words:
        nlp.vocab[w].is_stop = True

    tokens = [token.text for token in my_doc if not token.is_stop] # Remove stop words

    # print('Original query: %s' % (query))
    # print()
    # print(tokens)

    return tokens
