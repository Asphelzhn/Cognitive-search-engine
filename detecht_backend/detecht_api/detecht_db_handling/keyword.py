from rest_framework.exceptions import ValidationError

from detecht_api.detecht_nlp.word_similarity import word_similarity
from detecht_api.models import Keywords, Keyword_distance, Pdf_Name_Keyword_Weight, Interacted_documents, \
    Pdf_Similarities, User_Keyword
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


# Henrik
# add weight between pdf name and keyword
def Add_Pdf_Name_Keyword_Weight(pdf, keyword, weight):
    new = Pdf_Name_Keyword_Weight(pdf_name=pdf, keyword=keyword, weight=weight)
    #print(keyword+"    "+ weight)
    if len(new.pdf_name) <=50:
        new.save()
    else:
        print("error")
    return


# Henrik & Carl

def Trending_docs(size):
    list = Interacted_documents.objects.all().values().order_by("pdf_name")
    pdf_name_lsit = Interacted_documents.objects.all().values("pdf_name").distinct()

    if size > len(pdf_name_lsit):
        size = len(pdf_name_lsit)

    P = 1  # how much should a preview be worth?
    D = 2  # how much should a download be worth?
    Finale_value_table = [0] * len(pdf_name_lsit)
    temp = date.today()
    dateNow = date_calc(temp)

    for row in list:
        if row.get("down_prev") == "Preview":
            for i in range(0, len(pdf_name_lsit)):

                if pdf_name_lsit[i].get("pdf_name") == row.get("pdf_name"):
                    value = P / (dateNow - date_calc(row.get("date")) + 1)
                    Finale_value_table[i] += value

        if row.get("down_prev") == "Download":
            for i in range(0, len(pdf_name_lsit)):
                if pdf_name_lsit[i].get("pdf_name") == row.get("pdf_name"):
                    value = D / (dateNow - date_calc(row.get("date")) + 1)
                    Finale_value_table[i] += value

    final_table = []
    for i in range(0, len(pdf_name_lsit)):
        final_table.append([pdf_name_lsit[i].get("pdf_name"), Finale_value_table[i]])
    final_table.sort(key=sortsecond, reverse=True)
    return_table = final_table[:size]
    return return_table


def date_calc(dateNow):
    datenow1 = int(dateNow.strftime("%d")) + 30 * (int(dateNow.strftime("%d")) - 1) + 365 * int(dateNow.strftime("%d"))
    return datenow1

# interact with document
def Preview_Document(pdf_name, userid, type):
    dateNow = date.today()
    if type == "Preview":
        new = Interacted_documents(pdf_name=pdf_name, date=dateNow, userid=userid, down_prev="Preview")
        new.save()
    elif type == "Download":
        new = Interacted_documents(pdf_name=pdf_name, date=dateNow, userid=userid, down_prev="Download")
        new.save()
    else:
        print("error")
    return

# def Download_Document(pdf_name1, userid1):
#     dateNow = date.today()
#     new = Interacted_documents(pdf_name=pdf_name1, date=dateNow, userid=userid1, down_prev="Download")
#     new.save()


def pdf_relevance(name):  # returns a array [pdf_name, relevance] that is ordered highest to lowest on relevance.
    focus_pdf = Pdf_Name_Keyword_Weight.objects.filter(pdf_name=name).values("keyword", "weight")

    pdf_list = Pdf_Name_Keyword_Weight.objects.values("pdf_name", "keyword", "weight").exclude(pdf_name=name).order_by(
        "pdf_name")

    relevance_table = []
    relevance = 0
    relevance_name = []
    relevance_value = []
    for i in pdf_list:
        PDF_word = i.get("keyword")

        for a in focus_pdf:
            focus_word = a.get("keyword")
            # print("sakerfunkar")
            if PDF_word == focus_word:
                # print("saker funkar")
                relevance += i.get("weight") * a.get("weight")
                # Såhär långt så funkar allt som det ska
        relevance_name.append(i.get("pdf_name"))
        relevance_value.append(relevance)
        relevance = 0
    # print(relevance_name)
    # print(relevance_value)

    relevance_table = []
    i_old = relevance_name[0]
    a = 0  # Hålla koll på index för relevance vaule
    b = 0  # Hålla koll på index relevance table
    relevance = 0
    for i in relevance_name:
        if i == i_old:
            if not len(relevance_table) == 0:
                relevance_table.pop(b)
            relevance += relevance_value[a]
            relevance_table.insert(b, [i, relevance])
            # print(str(relevance) + "   " + i)
            # i_old=i
        else:
            relevance = 0
            b = +1
            # i_old = i
            # relevance += relevance_value[a]
            relevance_table.insert(b, [i, relevance_value[a]])
        i_old = i
        a += 1

    final_list = []
    for num in relevance_table:
        if num not in final_list:
            final_list.append(num)

    final_list.sort(key=sortsecond, reverse=True)
    return final_list


# Henrik

def sortsecond(val):
    return val[1]


def add_pdf_similarities(pdf1):
    similarity_list = pdf_relevance(pdf1)
    #print(similarity_list)
    for item in similarity_list:
        Pdf_Similarities.objects.update()
        a = item[0].get("pdf_name")
        b = item[1].get("similarity")
       # print(pdf1)
        new = Pdf_Similarities(document_name1=pdf1, document_name2=a, similarity=b)
        new.save()
    return


def add_all_pdf_similarities():
    all_files = Pdf_Name_Keyword_Weight.objects.all().values_list("pdf_name").distinct()
    # Not sure if it's okay to pick it up from here but i think it should work
    for object in all_files:
        object = object.get("pdf_name")
        add_pdf_similarities(object)
    return



def add_user_keyword(id, key):
    new = User_Keyword(userID=id, keyword=key)
    new.save()
    return


