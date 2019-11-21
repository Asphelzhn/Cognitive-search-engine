# from detecht_api import models
from random import Random
from detecht_api import models
from detecht_api.detecht_db_handling.search_table.standardize_query import \
    standardize_query
import time
from datetime import datetime
# Import commented since it is not used in file and tests are complaining
# about it but i dont want to remove it completely //Jakob
# from detecht_api.models import Searches_Database

"""
Edward and Severn
"""


# This is the api using for adding a new row into database.
# If there is no user_id, just set id as null.
def add_api(userid, query, date, score):

    standardized_query = standardize_query(query)
    if(date is None):

        # date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        date = datetime.now()

    models.Searches_Database.objects.create(user_id=userid,
                                            search_date=date,
                                            search_query=query,
                                            standardized_search_query
                                            =standardized_query,
                                            search_score=score)

    # obj = Searches_Database(user_id=id, search_date=date,
    #                        search_query=query,
    #                        standardized_search_query
    #                        =standardized_query,
    #                        search_score=2)
    # obj.save()


# This is the example using add_row method to add new row into database.
if __name__ == '__main__':
    query = ["Sherlock Holmes", "she is always the woman",
             "I have seldom heard him mention herunder any other name",
             "Irene Adler",
             "the most perfect reasoning and observing machine"]
    for i in query:
        for j in range(1, 5):
            score = Random().randint(1, 10)
            add_api(userid=j, query=i, date=None, score=score)
            time.sleep(5)
    print(models.Searches_Database.objects.all())
