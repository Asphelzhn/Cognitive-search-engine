from detecht_api import models
from detecht_db_handling.search_table.standardize_query import standardize_query
import time


# add new row into database. If there is no user_id, just set id as null.
def add_row(query, id):
    standardized_query = standardize_query(query)
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    obj = models.Searches_Database(user_id=id, search_date=date, search_query=query,
                                   standardized_search_query=standardized_query)
    obj.save()


if __name__ == '__main__':
    query = ["Sherlock Holmes", "she is always the woman",
             "I have seldom heard him mention herunder any other name", "Irene Adler",
             "the most perfect reasoning and observing machine"]
    for i in query:
        for j in range(1, 6):
            add_row(i, j)
    print(models.Searches_Database.objects.all())
