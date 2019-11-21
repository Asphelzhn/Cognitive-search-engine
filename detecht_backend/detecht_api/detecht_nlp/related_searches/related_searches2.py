import spacy
import time
from spacy.attrs import LOWER, POS, ENT_TYPE, IS_ALPHA
from spacy.tokens import Doc
import numpy

nlp = spacy.load("en_core_web_sm")
maxGram = 4

def delete_word(doc, index):
    del doc[index]
    return doc


def generate_one_new_word(doc,number):
    length = len(doc)
    if(length > maxGram):
        lowerIndex = length-maxGram
    else:
        lowerIndex = 0

    span = doc[lowerIndex:length]
    textList = doc[0:lowerIndex]

    "look over the data structure here"
    queryText = queryDatabase(span,1, number)

    return textList+queryText


def generate_two_new_word(doc, number):
    length = len(doc)
    print(length)
    thisGram=maxGram-1
    if (length > thisGram):
        lowerIndex = length - thisGram
    else:
        lowerIndex = 0

    span = doc[lowerIndex:length]
    textList = doc[0:lowerIndex]

    queryText = queryDatabase(span, 2, number)

    return textList+queryText



def queryDatabase(text, numberOfExtraWords, numOfQueries):
    i=len(text)
    list=[]
    list.append(text)
    while(i>0):
        #append to list
        print("Query")
        i=i-1
    #Retun list of texts with probabilities
    return list


def generateRelatedSearches(text):
    list = string_to_list(text)
    listDelete = delete_word(list.length)
    oneWordDeletePlusOne = generate_one_new_word(listDelete,1)
    oneWordDeletePlusTwo = generate_two_new_word(listDelete,1)
    oneWordAdded = generate_one_new_word(list,1)
    returnList= oneWordDeletePlusOne+oneWordDeletePlusTwo+oneWordAdded
    return returnList


def string_to_list(text):
    doc = nlp(text)
    list=[]
    for word in doc:
        list.append(word.text)
    return list

def main():
    text="hej jag heter"
    text=string_to_list(text)
    print(text)
    doc =delete_word(text,2)
    print(doc)
    t3=time.time()
    print(generate_two_new_word(["how", "are", "you"],1))
    t4=time.time()


    # doc =nlp("are you and somebody")
    # print(generate_one_new_word(doc,1))
    # doc = nlp("are you and")
    # print(generate_one_new_word(doc,1))
    # doc = nlp("are you")
    # print(generate_one_new_word(doc,1))
    # doc = nlp("are")
    # print(generate_one_new_word(doc,1))
    # print(type(generate_one_new_word(doc,1)))



if __name__ == '__main__':
    main()




