from MovableObject import MovableObject
class Animation:
    def __init__(self):
        self.__counter = 0
        self.__sprites = game_objects_data[id]['sprites']
        self.__current_sprite = self.__sprites['idle']

    def get_animation_move(self, velocity_vector: [float, float]):
        if self.__counter >=60:
            self.__counter=0
        if velocity_vector == [0, 0]:
            self.__counter = 0
            self.__current_sprite = self.__sprites['idle']
        if velocity_vector == [1, 0]:
            self.__current_sprite = self.__sprites["right"][self.__counter // (60 / len(self.__sprites["right"]))]
            self.__counter += 1
        if velocity_vector == [-1, 0]:
            self.__current_sprite = self.__sprites["left"][self.__counter // (60 / len(self.__sprites["right"]))]
            self.__counter += 1
        if velocity_vector == [0, 1]:
            self.__current_sprite = self.__sprites["up"][self.__counter // (60 / len(self.__sprites["right"]))]
            self.__counter += 1
        if velocity_vector == [0, -1]:
            self.__current_sprite = self.__sprites["down"][self.__counter // (60 / len(self.__sprites["right"]))]
            self.__counter += 1
        return self.__current_sprite
