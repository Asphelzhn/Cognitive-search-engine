from detecht_api.detecht_nlp.word_similarity import word_similarity
from detecht_api.models import Keywords
from detecht_api.models import Keyword_distance

#add keyword in db, if keyword alerady exists it is not added. If added true is returned. if it is in db False is returned
def addKeyword(keyword):
    keyword, created = Keywords.objects.get_or_create(word=keyword)

    if created: #True if keyword is added and does not exist in db
        keyword.save()
        #run similarity for all Query
        allKeywords = Keywords.objects.exclude(word=keyword)

        for word in allKeywords:
            KeywordSimilarity(keyword, word.word, word.id)
        return True
    return False

#add similarity for keyword.
def KeywordSimilarity(keyword1, keyword2, keywordId2):
    newDistance = Keyword_distance(id_1=Keywords.objects.get(word=keyword1).id, id_2=keywordId2, similarity=word_similarity(keyword1, keyword2))
    newDistance.save()
    return
