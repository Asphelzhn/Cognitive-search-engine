import tfidf

# TEXTS
text1 = "the cat sat on my face"
text2 = "the dog sat on my bed"

tokens1 = tfidf.tokenizewords(text1)
tokens2 = tfidf.tokenizewords(text2)
print(tokens1)
print(tokens2)

# Dictionarytest
dictionary = tfidf.createdict([tokens1, tokens2])
print(dictionary)
wordWeightsZero1 = tfidf.weightzero(dictionary)
wordWeightsZero2 = tfidf.weightzero(dictionary)
wordWeightsZero3 = tfidf.weightzero(dictionary)
print()
print("Wordweights:")
print(wordWeightsZero1)
print()
print("tokenFrequency")
termWordWeights1 = tfidf.termfrequency(tokens1,wordWeightsZero1)
termWordWeights2 = tfidf.termfrequency(tokens2, wordWeightsZero2)
print(termWordWeights1)
print(termWordWeights2)

# TF test
print("TF:")
tf1 = tfidf.computeTF(termWordWeights1, tokens1)
tf2 = tfidf.computeTF(termWordWeights1, tokens2)
print(tf1)
print(tf2)

# IDF Test
print()
print("IDF")
IDF = tfidf.computeIDF([termWordWeights1,termWordWeights2])
print(IDF)

# TFIDF test
print()
print("TFIDF")
TFIDF1=tfidf.computeTFIDF(tf1,IDF)
TFIDF2=tfidf.computeTFIDF(tf2,IDF)
print(TFIDF1)
print(TFIDF2)


#TFIDF test of main
print()
print()
print("main test:")
s = tfidf.computeTFIDFmain([text1, text2])
print(s)

print(s[0])

# TFIDF Test of dictionary to tuple
t = tfidf.dictionaryToSortedTuple(s[0])
print(t)
