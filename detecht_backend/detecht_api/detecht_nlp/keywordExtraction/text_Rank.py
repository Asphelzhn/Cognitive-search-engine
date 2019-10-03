import spacy

# use en_core_web_sm as model
nlp = spacy.load('en_core_web_sm')

content = '''
The Wandering Earth, described as China’s first big-budget science fiction thriller, quietly made it onto screens at AMC theaters in North America this weekend, and it shows a new side of Chinese filmmaking — one focused toward futuristic spectacles rather than China’s traditionally grand, massive historical epics. At the same time, The Wandering Earth feels like a throwback to a few familiar eras of American filmmaking. While the film’s cast, setting, and tone are all Chinese, longtime science fiction fans are going to see a lot on the screen that reminds them of other movies, for better or worse.
'''

doc = nlp(content)

# print the sentences
for sents in doc.sents:
    print(sents.text)
print("*"*30)
# just consider noun,propn,verb
candidate_pos = ['NOUN', 'PROPN', 'VERB']
sentences = []
​
# optional keyword
for sent in doc.sents:
    selected_words = []
    for token in sent:
        if token.pos_ in candidate_pos and token.is_stop is False:
            selected_words.append(token)
    sentences.append(selected_words)
​
print(sentences)

