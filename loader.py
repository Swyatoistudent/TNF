import json

GAME_DATA_PATH = ''

with open(GAME_DATA_PATH, 'r') as gd_f:
    game_objects_data = json.loads(gd_f.read())
