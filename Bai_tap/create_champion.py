import json
import os


def read_names():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "..\Bai_tap\Game_Data\\names.json")
    file = open(filename)
    read_file = file.read()
    names = json.loads(read_file)
    return names













