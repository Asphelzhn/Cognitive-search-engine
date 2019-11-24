from detecht_api.detecht_nlp.autocompleteWords import n_gram
import re

def test():
    query = "the"
    #output = re.sub('\n+', " ", n_gram.get_result(query))

    print(n_gram.get_result(query))
