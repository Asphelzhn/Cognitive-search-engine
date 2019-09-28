import json, requests, os
from elasticsearch import Elasticsearch


def insert_one_file (json)
    res = requests.get('http://localhost:8000')
    print (res.content)
    es = Elasticsearch([{'host': 'localhost', 'port': '8000'}])




def insert_files (directory="Standard")
    res = requests.get('http://localhost:8000')
    print (res.content)
    es = Elasticsearch([{'host': 'localhost', 'port': '8000'}])

    i=1;

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            f = open(filename)
            docket_content = f.read()
            # Send the data into es
            es.index(index='myindex', ignore=400, doc_type='docket',
                     id=i, body=json.loads(docket_content))
            i = i + 1

