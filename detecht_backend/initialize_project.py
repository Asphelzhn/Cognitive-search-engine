from elasticsearch import Elasticsearch
from detecht_api.django_setup import initialize_django
from detecht_api.detecht_nlp.autocompleteWords import upload_n_gram
es = Elasticsearch()

initialize_django()
es.indices.delete(index='db', ignore=[400, 404])
# ignore 400 cause by IndexAlreadyExistsException when creating an index
es.indices.create(index='db', ignore=400)
mapping = {
    "properties": {
        "pdf_name": {
            "type": "keyword"
        }
    }
}
es.indices.put_mapping(index='db', body=mapping)

upload_n_gram.upload()
