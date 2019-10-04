import json


# takes in json file and attribute, returns txt file with extracted attribute
def json_to_plaintext(json_file, attribute):
    json_tmp = json.loads(json_file.read())
    attr = json_tmp[attribute]  # collect attribute
    txt_file = open("json_attribute.txt", "w+")
    attr = str(attr)  # make string of object
    txt_file.write(attr)
    txt_file.close()

    return txt_file
