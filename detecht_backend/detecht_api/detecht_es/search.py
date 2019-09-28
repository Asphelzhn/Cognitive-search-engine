import json, requests, os
from elasticsearch import Elasticsearch

# res = requests.get('http://localhost:8000')
# print(res.content)
es = Elasticsearch([{'host': 'localhost', 'port': '8000'}])


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
    return es.search(index="DB", doc_type="doc", body=body)


# Should handle both single and multiple searches.
def multi_search(query, size=1):
    body = {
        "fields": ["title"],
        "size": size,
        "query": {
            "query_string": {
                "fields": ["file.content", "file.file.name"],
                "query": query
            }
        }
    }
    return es.search(index="DB", doc_type="doc", body=body)


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

    return es.search(index="DB", doc_type="doc", body=body)
