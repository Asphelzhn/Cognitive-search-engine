import json, requests, os

from elasticsearch import Elasticsearch

""" Jakob and Henrik
    How to insert data into es"""


es = None
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
if es.ping():
    print('Connected to elasticsearch')
else:
    print('Could not connect to elasticsearch')


json_string = '{"title":"Rupert", "age": 25, "desig":"developer"}'


def get_file(filename):
    f = open(filename+".json", "r")
    if f.mode == 'r':
        contents = f.read()
    print(contents)
    return contents


#get_file("test")


# not sure on how the tell it that it's supposed to go for the index db in our ES stack. but this may work.
def inject_one_file(json):
    es.indices.refresh(index="db")  # refreshes the index
    doc_count = es.cat.count(index="db", params={"format": "json"})
    doc_id_tmp = doc_count[0]["count"] #Counts the number of ids in the index, Returns an array of some sort
    doc_id = int(doc_id_tmp) + 1
    es.index(index="db", doc_type="doc", id=doc_id, body=json)

def inject_by_name(filename):
    inject_one_file(get_file(filename))


# this has some way to go to get to working condition //Henrik & jakob
def inject_files(directory="Standard"):
    es.indices.refresh(index="db")  # refreshes the index
    i = (es.cat.count(index="db")) + 1

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            f = open(filename)
            docket_content = f.read()
            # Send the data into es
            es.index(index='myindex', ignore=400, doc_type='docket',
                     id=i, body=json.loads(docket_content))
            i = i + 1

inject_by_name("test")
