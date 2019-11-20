import spacy

nlp = spacy.load("en_core_web_md")


""""
Henrik
"""


# it is possible to have the function modular for if it should use the small,medium or large spacey package but i
# dont think we will gain any efficiency by splitting it up, added variation will require more data space or that we
# load from spacey every time we compare words, i think it's better to use the same package every time to reduce the
# amount of operations.

def word_similarity (word1, word2, size="md"):
    token1 = nlp(word1)
    token2 = nlp(word2)

    return token1.similarity(token2)
