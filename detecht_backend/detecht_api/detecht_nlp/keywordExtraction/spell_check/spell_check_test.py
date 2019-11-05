import detecht_api.detecht_nlp.keywordExtraction.spell_check.spell_check as spell
import time
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

word=spell.words()

t0 = time.time()
he = spell.correction("sdzxfcgvhbjnkmlösdfcgvh")
t1 = time.time()
print(t1-t0)
print(he)

