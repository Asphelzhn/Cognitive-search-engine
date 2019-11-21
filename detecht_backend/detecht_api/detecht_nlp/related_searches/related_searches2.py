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


def generate_one_new_word(doc,number, textsThatCantbeUsed):
    length = len(doc)
    if(length > maxGram):
        lowerIndex = length-maxGram
    else:
        lowerIndex = 0

    span = doc[lowerIndex:length]
    textList = doc[0:lowerIndex]

    "look over the data structure here"
    queryText = queryDatabase(span,1, number)
    # Compare textList+queryText with text That cant be used
    #Make it string
    return textList+queryText


def generate_two_new_word(doc, number, textsThatCantbeUsed):
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
    #Compare textList+queryText with text That cant be used
    #Make ut string
    return textList+queryText



def queryDatabase(text, numberOfExtraWords, numOfQueries):
    list=[]
    list.append(text)
    i=0
    while(i<len(text)):
        i=i+1
        #append to list
        # remove

        print("Query")
    #Retun list of texts with probabilities
    return list

def compareWordList(queryReturn, wordsThatCantBeUsed):
    for i in wordsThatCantBeUsed:
        if(queryReturn==i):
            return False
    return True



def generateRelatedSearches(text):
    list = string_to_list(text)
    textsThatCantBeUsed=[]
    textsThatCantBeUsed.append(list)

    if(len(list)>1):
        listDelete = delete_word(list.length)
    else:
        listDelete=list

    oneWordDeletePlusOne = generate_one_new_word(listDelete,1,textsThatCantBeUsed)
    textsThatCantBeUsed.append(oneWordDeletePlusOne)

    oneWordDeletePlusTwo = generate_two_new_word(listDelete,1,textsThatCantBeUsed)
    oneWordDeletePlusOne.append(oneWordDeletePlusTwo)

    oneWordAdded = generate_one_new_word(list,1,textsThatCantBeUsed)
    returnList= oneWordDeletePlusOne+oneWordDeletePlusTwo+oneWordAdded
    return returnList


def string_to_list(text):
    doc = nlp(text)
    list=[]
    for word in doc:
        list.append(word.text)
    return list

def list_to_string(list):
    str1 = ''.join(list)
    return str1

def main():
    text="hej jag heter"
    text=string_to_list(text)
    print(text)
    doc =delete_word(text,2)
    print(doc)
    t3=time.time()
    print(generate_two_new_word(["how", "are", "you"],2,["how"]))
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




