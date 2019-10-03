import json, requests, os
from elasticsearch import Elasticsearch

# res = requests.get('http://localhost:8000')
# print(res.content)
es = None
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
if es.ping():
    print('Connected to elasticsearch')
else:
    print('Could not connect to elasticsearch')


def single_search(query):
    body = {
        "fields": ["title"],
        "size": 1,
        "query": {
            "query_string": {
                "fields": ["file.content", "file.file.name"],
                "query": query
            }
        }
    }
    return es.search(index="db", doc_type="doc", body=body)


# Should handle both single and multiple searches.
def search(query, size=1):
    body = {
        "_source": ["title"],
        "size": size,
        "query": {
            "query_string": {
                "query": query
            }
        }
    }

    res = es.search(index="db", body=body)
    return res


def format_search(result):
    titles = list()
    for hit in res['hits']['hits']:
        title = "%(title)s" % hit["_source"]
        titles.append(title)
    return titles


search("Rupert")


def formated_search(query, size=1):
    body = {
        "_source": ["file.file.filename"],
        "query": {
            "query_string": {
                "fields": ["file.content", "file.file.name"],
                "query": query,
                "size": size
            }
        }
    }

    return es.search(index="db", doc_type="doc", body=body)
