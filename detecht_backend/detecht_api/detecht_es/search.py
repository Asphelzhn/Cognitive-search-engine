import json, requests, os
from elasticsearch import Elasticsearch
from detecht_api.detecht_converter.jsonclass import JsonClass

""" Jakob and Henrik
    How to search after data from es"""

# res = requests.get('http://localhost:9200')
# print(res.content)
es = None
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
if es.ping():
    print('Connected to elasticsearch')
else:
    print('Could not connect to elasticsearch')


# Should handle both single and multiple searches.
def search(query, size=100):
    body = {
        "size": size,
        "query": {
            "query_string": {
                "fields": ["title^10", "pdf_name^1", "pages^1", "keywords^8"],
                "query": query,

            }
        }
    }
    es.indices.refresh(index="db")
    res = es.search(index="db", body=body)
    results = list()
    hits = 0
    for hit in res['hits']['hits']:
        hits = hits + 1
        j_class = JsonClass.init_from_json(json.dumps(hit["_source"]))
        results.append(j_class)
    return {"hits": hits, "results": results, "time": res["took"]}


# Should handle both single and multiple searches.
def get_pdf(query):
    body = {
        "size": 1,
        "query": {
            "query_string": {
                "fields": ["pdf_name"],
                "query": query,

            }
        }
    }
    es.indices.refresh(index="db")
    res = es.search(index="db", body=body)
    j_class = JsonClass.init_from_json(json.dumps(res['hits']['hits'][0]["_source"]))
    return {"j_class": j_class}


def formated_search(query, size=1):
    body = {
        "_source": ["title"],
        "size": size,
        "query": {
            "query_string": {
                "fields": ["title^10", "pdf_name^1", "pages^1", "keywords^8"],
                "query": query,

            }
        }
    }

    res = es.search(index="db", body=body)
    print(res)
    titles = list()
    for hit in res['hits']['hits']:
        title = "%(title)s" % hit["_source"]
        titles.append(title)
    return titles

