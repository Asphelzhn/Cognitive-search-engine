from elasticsearch import Elasticsearch

""" Jakob and Henrik
    How to insert data into es"""


es = None
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
if es.ping():
    print('Inject connected to Elasticsearch')
else:
    print('Inject could not connect to Elasticsearch')


def get_file(filename):
    f = open(filename, "r")
    if f.mode == 'r':
        contents = f.read()
    return contents


# not sure on how the tell it that it's supposed to go for the index
# db in our ES stack. but this may work.
def inject_one_file(json_obj):
    es.indices.refresh(index="db")  # refreshes the index
    es.index(index="db", doc_type="_doc", body=json_obj)


def inject(names):
    for name in names:
        inject_one_file((get_file(name)))


def inject_by_name(filename):
    inject_one_file(get_file(filename))


def delete_from_index(filename):
    es.indices.refresh(index="db")
    body = {
        "query": {
            "term": {
                "pdf_name": filename
            }
        }
    }
    es.delete_by_query(index="db", body=body)
