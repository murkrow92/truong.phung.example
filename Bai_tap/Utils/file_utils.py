import json
import os


def read_all_champion_config():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "../Game_Data/all_champion_config.json")
    file = open(filename)
    read_file = file.read()
    all_champion_config = json.loads(read_file)
    return all_champion_config


def read_champion_data(file_name):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "../Game_Data/%s.json" % file_name)
    file = open(filename)
    read_file = file.read()
    champion = json.loads(read_file)
    return champion
