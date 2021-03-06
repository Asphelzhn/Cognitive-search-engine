"""
@author: Samuel
@file:
@time: 2019/11/6 10:01
@desc: Using levehnstein distance for spell check
"""
import time
import detecht_api.detecht_nlp.spell_check.spell_check as spell

t0 = time.time()

t1 = time.time()
print("Import time: " + str(t1 - t0))


class spellCheck4SearchWord():
    def spell_check_api(self, text):
        """API for spell_check algorithm

        :param text: word that is being corrected
        :return: suggested_spell_check most relevant spell_check word
        """
        suggested_spell_check = spell.correction(text)
        return suggested_spell_check

    def upload_first_time(self):
        spell.uploadTxt(open(
            "detecht_api/detecht_nlp/spell_check/big.txt").read())
        print("uploaded")

    def upload_new_text(self, text):
        spell.uploadTxt(text)
        print("uploaded")


''' Example of spell correction with timing
'''
if __name__ == '__main__':

    t1 = time.time()
    text = input("Enter something wrong: ")
    t2 = time.time()
    suggestions = spell.candidates(text)
    t3 = time.time()
    he = spell.correction(text)
    t4 = time.time()
    print("Suggestion time: " + str(t3 - t2))
    print("Spell correction time: " + str(t4 - t3))
    print("Suggestions: " + str(suggestions))
    print("The correct one: " + str(he))
    print("Suggestion probability")
    for s in suggestions:
        print(spell.P(s))
