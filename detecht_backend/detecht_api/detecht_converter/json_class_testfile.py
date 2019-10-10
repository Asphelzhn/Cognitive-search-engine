from json_class import *


def get_file(filename):
    f = open(filename+".json", "r")
    if f.mode == 'r':
        contents = f.read()
    return contents


json_file = get_file("json_class_json_test_file")
json_class_instance = json_class(json_file)
print(json_class_instance.get_full_text())
