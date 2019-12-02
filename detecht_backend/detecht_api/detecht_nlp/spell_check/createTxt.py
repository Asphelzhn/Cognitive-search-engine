import spacy
import shutil
import os
from os import path

nlp = spacy.load("en_core_web_sm")


def creteTxt(arrayOfTxt):
    if path.exists("temp.txt"):
        shutil.copyfile("temp.txt", "tempcopy.txt")
    f = open("tempcopy.txt", "a")

    for i in arrayOfTxt:
        docx = nlp(i)
        for sentence in docx.sents:
            if (5 < len(sentence.text.split(' ')) < 30
                    and (sum(c.isalpha() for c in str(sentence)) / sum(
                        c != " " for c in str(sentence))) > 0.75):
                f.write(sentence.text)
    f.write(" ")
    f.close()
    if path.exists("temp.txt"):
        os.remove("temp.txt")
    os.rename("tempcopy.txt", "temp.txt")
