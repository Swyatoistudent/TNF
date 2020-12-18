import random


class Level:

    def __init__(self):
        self.__rooms = game_objects_data[id]['rooms']
        self.__current_room = 0

    def get_map(self):
        return [
            [random.choice(self.__rooms), random.choice(self.__rooms), random.choice(self.__rooms)],
            [random.choice(self.__rooms), random.choice(self.__rooms), random.choice(self.__rooms)],
            [random.choice(self.__rooms), random.choice(self.__rooms), random.choice(self.__rooms)],
        ]
