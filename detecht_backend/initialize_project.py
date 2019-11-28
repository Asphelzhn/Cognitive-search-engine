from elasticsearch import Elasticsearch
from detecht_api.detecht_nlp.autocompleteWords import upload_n_gram
es = Elasticsearch()


es.indices.delete(index='db', ignore=[400, 404])
# ignore 400 cause by IndexAlreadyExistsException when creating an index
es.indices.create(index='db', ignore=400)

upload_n_gram.upload()
