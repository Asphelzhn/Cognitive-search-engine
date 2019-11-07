from heapq import nlargest

from detecht_api.detecht_nlp.word_similarity import word_similarity
from detecht_api.models import Keywords, Keyword_distance, Pdf_Name_Keyword_Weight, Pdf_Similarities, Document


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


# Henrik
# add weight between pdf name and keyword
def Add_Pdf_Name_Keyword_Weight(pdf, keyword1, weight1):
    new = Pdf_Name_Keyword_Weight(pdf_name=pdf, keyword=keyword1, weight=weight1)
    new.save()
    return


def pdf_relevance(pdf_name):
    focus_pdf = Pdf_Name_Keyword_Weight.objects.filter(name=pdf_name).values("keyword", "weight")

    pdf_list = Pdf_Name_Keyword_Weight.objects.values("pdf_name", "keyword", "weight").exclude(name=pdf_name)

    relevance_table = []
    relevance = 0
    for i in pdf_list:
        for compareKey in pdf_list(i).keys:
            for fKey in focus_pdf.keys:
                if fKey == compareKey:
                    relevance = + pdf_list(i).weight(compareKey) * focus_pdf.weight(fKey) / 2

        relevance_table.append([pdf_list(i).pdf_name, relevance])
        relevance = 0

    # relevance_table = nlargest(size, relevance_table, key=relevance)
    relevance_table.sort(key=sortsecond(relevance_table), reverse=True)

    return relevance_table


def sortsecond(val):
    return val[1]


def add_pdf_similarities(pdf1):
    similarity_list = pdf_relevance(pdf1)
    for object in similarity_list:
        new = Pdf_Similarities(document_name1=pdf1, document_name2=object[0], Similarity=object[1])
        new.save()
    return


def add_all_pdf_similarities():
    all_files = Pdf_Name_Keyword_Weight.objects.values("pdf_name")
    # Not sure if it's okay to pick it up from here but i think it should work
    for object in all_files:
        add_pdf_similarities(object)
