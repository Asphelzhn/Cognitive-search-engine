import json, requests, os

from elasticsearch import Elasticsearch



es = None
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
if es.ping():
    print('Connected to elasticsearch')
else:
    print('Could not connect to elasticsearch')


json_string = '{"title":"Rupert", "age": 25, "desig":"developer"}'


# not sure on how the tell it that it's supposed to go for the index db in our ES stack. but this may work.
def inject_one_file(json):
    es.indices.refresh(index="db")  # refreshes the index
    es.index(index="db", doc_type="doc", body=json)
    print(es.cat.count(index="db",params={"format": "json"}))  # Counts the number of ids in the index, Returns an array of some sort


inject_one_file(json_string)


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

# def insert_document
