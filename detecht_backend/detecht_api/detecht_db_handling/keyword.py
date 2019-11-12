from detecht_api.detecht_nlp.word_similarity import word_similarity
from detecht_api.models import Keywords, Keyword_distance, Pdf_Name_Keyword_Weight, Interacted_documents
from datetime import date


# add keyword in db, if keyword alerady exists it is not added. If added true is returned. if it is in db False is returned
def addKeyword(keyword):
    keyword, created = Keywords.objects.get_or_create(word=keyword)

    if created:  # True if keyword is added and does not exist in db
        keyword.save()
        # run similarity for all Query
        allKeywords = Keywords.objects.exclude(word=keyword)

        for word in allKeywords:
            KeywordSimilarity(keyword, word.word, word.id)
        return True
    return False


# add similarity for keyword.
def KeywordSimilarity(keyword1, keyword2, keywordId2):
    newDistance = Keyword_distance(id_1=Keywords.objects.get(word=keyword1).id, id_2=keywordId2,
                                   similarity=word_similarity(keyword1, keyword2))
    newDistance.save()
    return


# add weight between pdf name and keyword
def Add_Pdf_Name_Keyword_Weight(pdf, keyword, weight):
    new = Pdf_Name_Keyword_Weight(pdf_name=pdf, keyword=keyword, weight=weight).d
    new.save()
    return

# Henrik & Carl

def Trending_docs(size):
    list = Interacted_documents.objects.all().values().order_by("pdf_name")
    pdf_name_lsit = Interacted_documents.objects.all().values("pdf_name").distinct()

    P = 1 # how much should a preview be worth?
    D = 2 # how much should a download be worth?
    Finale_value_table=[0] * len(pdf_name_lsit)
    temp = date.today()
    dateNow = date_calc(temp)

    for row in list:
        if row.get("down_prev") == "Preview":
            for i in range(0, len(pdf_name_lsit)):

                if pdf_name_lsit[i].get("pdf_name") == row.get("pdf_name"):

                    value = P/(dateNow-date_calc(row.get("date"))+1)
                    Finale_value_table[i] += value

        if row.get("down_prev") == "Download":
            for i in range(0, len(pdf_name_lsit)):
                if pdf_name_lsit[i].get("pdf_name") == row.get("pdf_name"):
                    value = D/(dateNow-date_calc(row.get("date"))+1)
                    Finale_value_table[i] += value

    final_table = ["",0] * len(pdf_name_lsit)
    for i in range(0, len(pdf_name_lsit)):
        final_table[i] = [pdf_name_lsit[i].get("pdf_name"), Finale_value_table[i]]



    #Needs to be sorted at this stage!!!
    return_table  = final_table[:size]
    return return_table


def date_calc(dateNow):
    datenow1 = int(dateNow.strftime("%d")) *30* int(dateNow.strftime("%d")) * 365*int(dateNow.strftime("%d"))
    return datenow1


# Henrik & Carl
def Preview_Document(pdf_name1, userid1):
    dateNow = date.today()
    new = Interacted_documents(pdf_name=pdf_name1, date=dateNow, userid=userid1, down_prev="Preview")
    new.save()


def Download_Document(pdf_name1, userid1):
    dateNow = date.today()
    new = Interacted_documents(pdf_name=pdf_name1, date=dateNow, userid=userid1, down_prev="Download")
    new.save()
