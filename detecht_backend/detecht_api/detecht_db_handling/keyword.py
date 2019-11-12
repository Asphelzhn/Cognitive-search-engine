from detecht_api.detecht_nlp.word_similarity import word_similarity
from detecht_api.models import Keywords, Keyword_distance, Pdf_Name_Keyword_Weight

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
    new = Pdf_Name_Keyword_Weight(pdf_name=pdf, keyword=keyword, weight=weight).d
    new.save()
    return

def Trending_docs(size):
    list = interacted_documents.objects.all().values().order_by("pdf_name")
    pdf_name_lsit = interated_docuemnts.object.all().values("pdf_name").Distinct()

    # antal preview en konstant = P
    # antal downloads en konstant = D
    #dividerat på dateNow-dateOld

    # trend_value = ( P * D ) / datenow_dateold
    #om preview

    #    += p/datediff

    #om download

     #   += d/datediff

    #Final table
    #pdf_name , trend_value