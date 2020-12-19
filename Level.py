import random
from Room import Room


class Level:

    def __init__(self):
        self.__rooms = game_objects_data[id]['rooms']
        self.__current_room = [0,0]

    def get_map(self):
        return [
            [Room(random.choice(self.__rooms)), Room(random.choice(self.__rooms)), Room(random.choice(self.__rooms))],
            [Room(random.choice(self.__rooms)), Room(random.choice(self.__rooms)), Room(random.choice(self.__rooms))],
            [Room(random.choice(self.__rooms)), Room(random.choice(self.__rooms)), Room(random.choice(self.__rooms))],
        ]
