from detecht_api.detecht_nlp import word_similarity
from detecht_api.models import Keywords
from detecht_api.models import Keyword_distance

#add keyword in db, if keyword alerady exists it is not added. If added true is returned. if it is in db False is returned
def addKeyword(keyword):
    if Keywords.add_keyword(keyword): #returns true if keyword is added in db
        #run similarity for all Query
        allKeywords = Keywords.objects.exclude(word=keyword)

        for word in allKeywords:
            KeywordSimilarity(Keywords.objects.get(word=keyword).id, word.id)
        return True
    return False

#add similarity for keyword.
def KeywordSimilarity(keywordId1, keywordId2):
    if Keyword_distance.add_keyword_distance(id1=keywordId1, id2=keywordId2, similarity=word_similarity(keywordId1, keywordId2)):
        return True #keyword combination was created
    return False #keyword combination was not created and similarity not updated
