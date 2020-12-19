from typing import List
from MovableObject import MovableObject
import IDamageable
from loader import game_objects_data


class Hero(MovableObject, IDamageable):
    def __init__(self, id: int, position: [int, int], type_name='Hero'):
        super(Hero, self).__init__(id, position, type_name=type_name)
        self.weapons = game_objects_data[id]['weapons']
        self.current_weapon = game_objects_data[id]['currnet_weapon']
        self.passiv_items = game_objects_data[id]['passiv_itemes']
        self.active_item = game_objects_data[id]['active_items']
        self.max_ammo_mod = game_objects_data[id]['max_ammo_mod']
        self.damage_mod = game_objects_data[id]['damage_mod']
        self.control = game_objects_data[id]['control']
        self.armor = game_objects_data[id]['armor']

    def get_info(self):
        return [self.max_hp, self.hp, self.armor, self.weapons, self.current_weapon, self.active_items]

    def get_damage(self, damage):
        # getting damage
        self._hp -= damage
        # animation call
