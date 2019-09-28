import json, requests, os
from elasticsearch import Elasticsearch



def single_search (query):
    res = requests.get('http://localhost:8000')
    print (res.content)
    es = Elasticsearch([{'host': 'localhost', 'port': '8000'}])
    return es.search(index="DB", body=query)


