import time
from detecht_api.detecht_nlp.spell_check import spell_check

t0 = time.time()
t1 = time.time()
text = input("Enter something wrong: ")
t2 = time.time()
suggestions = spell_check.candidates(text)
t3 = time.time()
he = spell_check.correction(text)
t4 = time.time()
print("Load database: " + str(t1-t0))
print("Suggestion time: " + str(t3-t2))
print("Spell correction time: " + str(t4-t3))
print("Suggestions: " + str(suggestions))
print("The correct one: " + str(he))
print("Suggestion probability")
for s in suggestions:
    print(spell_check.P(s))
