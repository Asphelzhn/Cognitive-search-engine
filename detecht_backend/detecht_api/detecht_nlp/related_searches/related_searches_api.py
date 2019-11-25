# encoding: utf-8
'''
@author: Samuel
@file: autocomplete_one_word_api.py
@time: 2019/11/25 17:17
@desc: Using N-gram to generate search suggestions
'''
from detecht_api.detecht_nlp.related_searches import related_searches2



class related_searches():
    def related_searches(self,text):
        # Takes input as string
        # Returns 3 different similar searches if those are found.
        # Otherwise fewer.
        # If no similiar search was found 0 is returnes
        related_searches = related_searches2.generateRelatedSearches(text)
        return related_searches


if __name__ == '__main__':
    related_searches2.main()