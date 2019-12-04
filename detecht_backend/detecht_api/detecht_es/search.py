import json
from elasticsearch import Elasticsearch
from detecht_api.detecht_converter.jsonclass import JsonClass

""" Jakob and Henrik
    How to search after data from es"""

es = None
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
if es.ping():
    print('Search connected to Elasticsearch')
else:
    print('Search could not connect to Elasticsearch')


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
    j_class = JsonClass.init_from_json(json.dumps(
        res['hits']['hits'][0]["_source"]))
    return {"j_class": j_class}


def formatted_search(query, size=1):
    body = {
        "_source": ["pdf_name"],
        "size": size,
        "query": {
            "query_string": {
                "fields": ["title^10", "pages^1", "keywords^8"],
                "query": query,

            }
        }
    }

    res = es.search(index="db", body=body)
    print(res)
    num_hits = res['hits']['total']['value']
    print(num_hits)
    titles = list()
    counter = 0
    for hit in res['hits']['hits']:
        if counter >= 10:
            break
        counter += 1
        title = "%(pdf_name)s" % hit["_source"]
        titles.append(title)
    return titles, num_hits
