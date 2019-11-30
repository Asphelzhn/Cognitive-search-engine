import spacy
import shutil
import os
from os import path


nlp = spacy.load("en_core_web_sm")


def creteTxt(arrayOfTxt):
    if path.exists("temp.txt"):
        dest=shutil.copyfile("temp.txt", "tempcopy.txt")
    f = open("tempcopy.txt", "a")

    for i in arrayOfTxt:
        print(1)
        docx=nlp(i)
        for sentence in docx.sents:
            print(2)
            print(len(str(sentence)))
            if 5 < len(sentence.text.split(' ')) < 30 and (sum(c.isalpha() for c in str(sentence)) / sum(c != " " for c in str(sentence))) > 0.75:
                print(3)
                f.write(sentence.text)
    f.write(" ")
    f.close()
    if path.exists("temp.txt"):
        os.remove("temp.txt")
    os.rename("tempcopy.txt","temp.txt")
