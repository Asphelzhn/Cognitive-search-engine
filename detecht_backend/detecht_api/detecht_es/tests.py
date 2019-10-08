from Insert_file import inject_one_file, inject_by_name
from search import search, formated_search


json_string = '{"title":"Kalle", "age": 27, "desig":"developer"}'


print("Inject json file by name")
inject_by_name("test")

print("Inject a json string")
inject_one_file(json_string)

print("Search for rupert with full result")
print(search("rupert"))
print("Search for Kalle with formated output")
print(formated_search("Kalle"))