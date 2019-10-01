import json


def test_message(message):
    return "Hello, message: " + message


def json_to_plaintext(jsonfile, attribute):

    read = jsonfile.read()
    json_as_string = json.loads(read)
    r = json_as_string[attribute]



    return r
