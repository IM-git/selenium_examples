import json


def read_file(way):
    with open(way) as text:
        data = json.load(text)
    return data
