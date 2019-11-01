from detecht_api.detecht_nlp.word_similarity import word_similarity
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
    newDistance = Keyword_distance(id_1=keywordId1, id_2=keywordId2, similarity=word_similarity(keywordId1, keywordId2))
    newDistance.save()
    return
