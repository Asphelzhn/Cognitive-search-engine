import spacy
import numpy as np
from scipy.spatial import distance
import gensim
import time
from gensim.models import KeyedVectors
# Load vectors directly from the file

print("start")
t0=time.time()
model = KeyedVectors.load("keyedvectors.model")
print(123)
t1=time.time()
model = KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin", binary=True)
t2=time.time()
print(123)
print(model.vector_size)
print(model.wv.vocab)
#model.save("keyedvectors.model")

nlp = spacy.load("en_core_web_sm")
print(123)


def related_searches(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    input_word=text
    for ent in doc.ents:
        print(ent.text, ent.label_)
    for token in doc:
        print("normal vector")
        print(type(token.vector))
        print(token.vector)
    # Format the input vector for use in the distance function
    # In this case we will artificially create a word vector from a real word ("frog")
    # but any derived word vector could be used


    # Format the vocabulary for use in the distance function
    ids = [x for x in nlp.vocab.vectors.keys()]
    print(ids)
    vectors = [nlp.vocab.vectors[x] for x in ids]
    #vectors = np.array(vectors)

    # *** Find the closest word below ***
    #closest_index = distance.cdist(p, vectors).argmin()
    #word_id = ids[closest_index]
    #output_word = nlp.vocab[word_id].text
    # output_word is identical, or very close, to the input word


def most_similar(word):
    return model.most_similar(word)

def similarSearch(text):
    doc=nlp(text)
    for ent in doc.ents:
        print(1)

def find_closest_word(doc):
    for token in doc:
        print(token.vector)
    p = np.array([nlp.vocab[input_word].vector])

def main():
    # related_searches("buying")
    print(1)
    print(2)
    doc = nlp("buying cat")
    t3=time.time()
    print(most_similar("cat"))
    t4=time.time()

    print(t1-t0)
    print(t2-t1)
    print(t3-t2)
    print(t4-t3)
    #most_similar(nlp)
    print("Similarity:", doc[0].similarity(doc[1]))
    # print(most_similar(nlp("buying")))


if __name__ == '__main__':
    main()