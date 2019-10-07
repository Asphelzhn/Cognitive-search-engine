import requests

requests.put("localhost:9200/db", data={"settings": {"index": {}}})

# curl -X PUT "localhost:9200/db" -H 'Content-Type: application/json' -d'{ "settings" : { "index" : { } }}'
