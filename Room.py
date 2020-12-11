class Room:
    def __init__(self, id: int):
        self.__id = id
        self.__description = game_objects_data[id]['room']

    @property
    def description(self):
        return self.__description

    def get_id(self):
        return self.__id
