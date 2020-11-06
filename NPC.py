import MovableObject


class NPC(MovableObject):
    def __init__(self, id: int, position: [int, int], type_name='NPC'):
        super(NPC, self).__init__(id, position, type_name=type_name)
        self.__attack_id = game_objects_data[id]['attack_id']
        self.__ai_type = game_objects_data[id]['ai_type']

    def ai(self):
        ais[self.__ai_type]()
