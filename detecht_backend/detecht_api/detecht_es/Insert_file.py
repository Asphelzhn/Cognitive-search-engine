import json, requests, os

from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': '8000'}])

# not sure on how the tell it that it's supposed to go for the index DB in our ES stack. but this may work.
def inject_one_file(json):
    es.indices.refresh(index="DB")  # refreshes the index
    newid = (es.cat.count(index="DB")) + 1  # Counts the number of ids in the index
    es.index(index="DB", doc_type="doc", id=newid, body=json)


# this has some way to go to get to working condition //Henrik & jakob
def inject_files(directory="Standard"):

    es.indices.refresh(index="DB")  # refreshes the index
    i = (es.cat.count(index="DB")) +1

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            f = open(filename)
            docket_content = f.read()
            # Send the data into es
            es.index(index='myindex', ignore=400, doc_type='docket',
                     id=i, body=json.loads(docket_content))
            i = i + 1



def insert_document