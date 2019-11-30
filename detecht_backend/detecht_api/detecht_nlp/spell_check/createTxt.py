import spacy

nlp = spacy.load("en_core_web_sm")


def creteTxt(arrayOfTxt):
    for i in arrayOfTxt:
        str=nlp(i)
        if