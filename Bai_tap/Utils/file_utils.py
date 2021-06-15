import json
import os


def read(file_name):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "../Game_Data/%s.json" % file_name)
    file = open(filename)
    read_file = file.read()
    champion = json.loads(read_file)
    return champion
