from elasticsearch import Elasticsearch
es = Elasticsearch()


es.indices.delete(index='db', ignore=[400, 404])
# ignore 400 cause by IndexAlreadyExistsException when creating an index
es.indices.create(index='db', ignore=400)

