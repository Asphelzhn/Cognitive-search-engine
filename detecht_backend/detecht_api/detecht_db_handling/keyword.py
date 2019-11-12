from detecht_api.detecht_nlp.word_similarity import word_similarity
from detecht_api.models import Keywords, Keyword_distance, Pdf_Name_Keyword_Weight, User_Keyword


# add keyword in db, if keyword alerady exists it is not added. If added true is returned. if it is in db False is returned
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


# add similarity for keyword.
def KeywordSimilarity(keyword1, keyword2, keywordId2):
    newDistance = Keyword_distance(id_1=Keywords.objects.get(word=keyword1).id, id_2=keywordId2, similarity=word_similarity(keyword1, keyword2))
    newDistance.save()
    return


# add weight between pdf name and keyword
def Add_Pdf_Name_Keyword_Weight(pdf, keyword, weight):
    new = Pdf_Name_Keyword_Weight(pdf_name=pdf, keyword=keyword, weight=weight)
    new.save()
    return



def add_user_keyword(id, key):
    new = User_Keyword(userID=id, keyword=key)
    new.save()
    return


