import math
import spacy
import operator
# Primitive function, solve this with spacy
def tokenizewords(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    tokenText=[]
    for token in doc:
        tokenText.append(token.text)
    return tokenText


# Capital letter doesn't work now
def createdict(differenttexts):
    wordset = differenttexts[0]
    for texts in differenttexts:
        wordset = set(wordset).union(texts)
    return wordset


# Adds weights of zero
def weightzero(wordset):
    dictionarytemp = dict.fromkeys(wordset, 0)
    return dictionarytemp


# Term frequency in document
def termfrequency(terms, dictionary1):
    for term in terms:
        dictionary1[term] += 1
    return dictionary1

# Computes the Term Frequency of all words in the dictionary by looking through the document
def computeTF(wordDict, bow):
    TFdict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        TFdict[word] = count/float(bowCount)
    return TFdict


def computeIDF(docList):
    idfdict = {}
    N = len(docList)
    # Counts the number of times a term is mentioned
    idfdict = dict.fromkeys(docList[0].keys(), 0)

    for doc in docList:
        for term, val in doc.items():
            if val > 0:
                idfdict[term] += 1

    for term, val in idfdict.items():
        idfdict[term] = math.log(N/float(val))
    return idfdict


def computeTFIDF(tfBOWs, idfs):
    tfidf = {}
    for word, val in tfBOWs.items():
        tfidf[word]= val*idfs[word];
    return tfidf


def dictionaryToSortedTuple(dictionary):
    theList = [(term,val) for term, val in dictionary.items()]
    theList.sort(key=operator.itemgetter(1), reverse=True)
    return theList


# Given string a few string docs, this function returns the weights of different terms
def computeTFIDFmain(docs):
    tokenArray = []
    amountdocs = len(docs)

    # Makes all docs into a list of terms
    for strings in docs:
        tokenArray.append(tokenizewords(strings))  # This variable should exist in entire document

    # Creates dictionary of all documents
    allTermsInDocs = createdict(tokenArray)  # This variable should exist in entire document

    # Counts the terms in each document and computes TF
    docTFdict=[]
    for x in range(amountdocs):
        tempDictionary=weightzero(allTermsInDocs)
        termFrequencyInDoc=termfrequency(tokenArray[x],tempDictionary)
        TF = computeTF(termFrequencyInDoc, tokenArray[x])
        docTFdict.append(TF) # This variable should exist in entire document

    # Computes document frequency for each word and the idf
    IDF = computeIDF(docTFdict) # This variable should exist in entire document

    # Compute TFIDF and put in list of tuple
    docTFIDfdict = [] # This variable should exist in entire document
    for x in range(amountdocs):
        temp = computeTFIDF(docTFdict[x], IDF)
        temp1=dictionaryToSortedTuple(temp)
        docTFIDfdict.append(temp1)

    return docTFIDfdict




