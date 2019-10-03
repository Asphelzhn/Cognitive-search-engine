import json, requests, os
from elasticsearch import Elasticsearch

# res = requests.get('http://localhost:9200')
# print(res.content)
es = None
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
if es.ping():
    print('Connected to elasticsearch')
else:
    print('Could not connect to elasticsearch')


# Should handle both single and multiple searches.
def search(query, size=1):
    body = {
        #"_source": ["title"],
        "size": size,
        "query": {
            "query_string": {
                "query": query
            }
        }
    }

    res = es.search(index="db", body=body)
    print(res)
    return res


def formated_search(query, size=1):
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
    print(res)
    titles = list()
    for hit in res['hits']['hits']:
        title = "%(title)s" % hit["_source"]
        titles.append(title)
    return titles


search("rupert")

