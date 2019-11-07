# from detecht_api import models
from detecht_api.detecht_db_handling.search_table.standardize_query import standardize_query
import time

from detecht_api.models import Searches_Database

"""
Edward and Severn
"""

# add new row into database. If there is no user_id, just set id as null.
def add(query, id):
    standardized_query = standardize_query(query)
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    search = Searches_Database()
    search.add_row(id, date, query,standardized_query,2)
    # obj = Searches_Database(user_id=id, search_date=date, search_query=query,standardized_search_query=standardized_query,search_score=2)
    # obj.save()


if __name__ == '__main__':
    query = ["Sherlock Holmes", "she is always the woman",
             "I have seldom heard him mention herunder any other name", "Irene Adler",
             "the most perfect reasoning and observing machine"]
    for i in query:
        for j in range(1, 6):
            add(i, j)
            time.sleep(5)
    # print(models.Searches_Database.objects.all())
