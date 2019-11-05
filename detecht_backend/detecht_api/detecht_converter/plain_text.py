import json
import os

"""
Oscar
"""


# takes in json file and attribute, returns txt file with extracted attribute
def json_to_plaintext(json_file):
    if os.path.exists("json_attribute.txt"):
        os.remove("json_attribute.txt")

    json_tmp = json.loads(json_file.read())
    attr = str
    attr = str(json_tmp["meta"])  # collect attribute
    txt_file = open("json_attribute.txt", "w+")
    attr = str(attr)  # make string of object
    txt_file.write(attr)
    txt_file.close()
    json_file.close()

    return txt_file
