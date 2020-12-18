import json

GAME_DATA_PATH = ''
AIS_PATH = ''

with open(GAME_DATA_PATH, 'r') as gd_f, open(AIS_PATH, 'r') as ais_f:
    game_objects_data = json.loads(gd_f.read())
    ais = json.loads(ais_f.read())
