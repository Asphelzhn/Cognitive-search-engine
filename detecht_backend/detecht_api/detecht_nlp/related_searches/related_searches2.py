import spacy
import time
import os
import django
from detecht_api.models import Search_Autocomplete

os.environ['DJANGO_SETTINGS_MODULE'] = 'detecht_backend.settings'

django.setup()

# from spacy.attrs import LOWER, POS, ENT_TYPE, IS_ALPHA
# from spacy.tokens import Doc
# import numpy

nlp = spacy.load("en_core_web_sm")
maxGram = 4


def delete_word(doc, index):
    newList = doc.copy()
    del newList[index]
    return newList


def generate_one_new_word(doc, number, textsThatCantbeUsed):
    queryText = queryDatabase(doc, 1, number, textsThatCantbeUsed)
    return queryText


def generate_two_new_word(doc, number, textsThatCantbeUsed):
    queryText = queryDatabase(doc, 2, number, textsThatCantbeUsed)
    return queryText


# numOfExtraWords < 3
def queryDatabase(querySplit, numberOfExtraWords,
                  numOfQueries, textsThatCantBeUsed):
    if (numberOfExtraWords > 3):
        return 0

    queryBeginning = []
    lengthOfQuery = len(querySplit)

    if (lengthOfQuery > 4):
        index = lengthOfQuery - 4
    else:
        index = 0
    tempQuery = list_to_string(querySplit)

    tempQuery = list_to_string(querySplit[index:lengthOfQuery])
    result = Search_Autocomplete.objects.filter(
        n_gram__istartswith=tempQuery)
    resultCount = result.count()

    while (resultCount < numOfQueries):
        tempQuery = list_to_string(querySplit[index:lengthOfQuery])
        # print(tempQuery)
        result = Search_Autocomplete.objects.filter(
            n_gram__istartswith=tempQuery)
        index = index + 1
        resultCount = result.count()
        if (index > lengthOfQuery):
            return 0

    if (index > 0):
        queryBeginning = querySplit[0:index - 1]

    gram_list = []
    for r in result:
        gram_list.append(r.n_gram)
    n2gram = []
    n3gram = []
    n4gram = []
    n5gram = []
    for g in gram_list:
        if g not in textsThatCantBeUsed:
            if len(g.split()) == 2:
                n2gram.append(g)
            elif len(g.split()) == 3:
                n3gram.append(g)
            elif len(g.split()) == 3:
                n3gram.append(g)
            elif len(g.split()) == 4:
                n4gram.append(g)
            elif len(g.split()) == 5:
                n5gram.append(g)

    # print(n2gram)
    # print(n3gram)
    # print(n4gram)
    # print(n5gram)

    # ERROR IN NUMBER OF EXTRAWORDS
    tempQueryLen = len(tempQuery.split())
    result_list = []
    if tempQueryLen == 1:
        if numberOfExtraWords == 2:
            result_list = n3gram[:numOfQueries]
        elif numberOfExtraWords == 1:
            result_list = n2gram[:numOfQueries]
        else:
            return 0
    elif tempQueryLen == 2:
        if numberOfExtraWords == 2:
            result_list = n4gram[:numOfQueries]
        elif numberOfExtraWords == 1:
            result_list = n3gram[:numOfQueries]
        else:
            return 0
    elif tempQueryLen == 3:
        if numberOfExtraWords == 2:
            result_list = n5gram[:numOfQueries]
        elif numberOfExtraWords == 1:
            result_list = n4gram[:numOfQueries]
        else:
            return 0
    elif tempQueryLen == 4:
        if numberOfExtraWords == 2:
            return 0
        elif numberOfExtraWords == 1:
            result_list = n5gram[:numOfQueries]
        else:
            return 0

    firstPart = list_to_string(queryBeginning)

    if (len(firstPart) > 0):
        firstPart = firstPart + " "

    return [firstPart + s for s in result_list]


def compareWordList(queryReturn, wordsThatCantBeUsed):
    for i in wordsThatCantBeUsed:
        if (queryReturn == i):
            return False
    return True


def generateRelatedSearches(text):
    if (text == ""):
        return 0

    list = string_to_list(text)
    textsThatCantBeUsed = []
    textsThatCantBeUsed.append(text)

    if (len(list) > 1):

        listDelete = delete_word(list, len(list) - 1)
    else:
        listDelete = list
    resultsToBeGenerated = 1
    oneWordDeletePlusOne = generate_one_new_word(listDelete,
                                                 resultsToBeGenerated,
                                                 textsThatCantBeUsed)

    if oneWordDeletePlusOne != 0:
        textsThatCantBeUsed = textsThatCantBeUsed + oneWordDeletePlusOne
    else:
        resultsToBeGenerated = resultsToBeGenerated + 1

    oneWordDeletePlusTwo = generate_two_new_word(listDelete,
                                                 resultsToBeGenerated,
                                                 textsThatCantBeUsed)
    if oneWordDeletePlusTwo != 0:
        textsThatCantBeUsed = textsThatCantBeUsed + oneWordDeletePlusTwo
        if len(oneWordDeletePlusTwo) == resultsToBeGenerated:
            resultsToBeGenerated = 1
        else:
            resultsToBeGenerated = resultsToBeGenerated - len(
                oneWordDeletePlusTwo)
    else:
        resultsToBeGenerated = resultsToBeGenerated + 1

    oneWordAdded = generate_one_new_word(list, resultsToBeGenerated,
                                         textsThatCantBeUsed)
    if oneWordAdded != 0:
        returnList = oneWordDeletePlusOne + oneWordDeletePlusTwo + oneWordAdded
    else:
        returnList = oneWordDeletePlusOne + oneWordDeletePlusTwo
    return returnList


def string_to_list(text):
    doc = nlp(text)
    list = []
    for word in doc:
        list.append(word.text)
    return list


def list_to_string(list):
    str1 = ' '.join(list)
    return str1


def main():
    # print(generate_two_new_word(["how", "are", "you"],2,["how"]))
    str = input('Enter your search: ')
    t3 = time.time()
    print(generateRelatedSearches(str))
    # print(generate_two_new_word(["what", "is"],10,["how"]))
    # print(list_to_string(["hej", "hur"]))
    t4 = time.time()
    print(t4 - t3)


if __name__ == '__main__':
    main()
