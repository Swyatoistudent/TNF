from MovableObject import MovableObject
import IDamageable
from loader import game_objects_data, ais


class NPC(MovableObject, IDamageable):
    def __init__(self, id: int, position: [int, int], type_name='NPC'):
        super(NPC, self).__init__(id, position, type_name=type_name)
        self.__attack_id = game_objects_data[id]['attack_id']
        self.__ai_type = game_objects_data[id]['ai_type']

    def ai(self):
        ais[self.__ai_type]()

    def get_damage(self, damage):
        # getting damage
        self._hp -= damage
        # animation call
