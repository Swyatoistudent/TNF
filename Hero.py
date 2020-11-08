from typing import List

import MovableObject

class Hero(MovableObject):
        def __init__(self,id : int,position:[int,int], type_name = 'Hero'):
            super(Hero,self).__init__(id,position,type_name=type_name)
            self.weapons = List[Weapon]
            self.current_weapon = Weapon
            self.passiv_items = List[PassivItem]
            self.active_items = List[ActiveItem]
            self.max_ammo_mod = game_objects_data[id]['max_ammo_mod']
            self.damage_mod = game_objects_data[id]['damage_mod']
            self.control = Control
            self.armor = game_onjects_data[id]['armor']
        def get_info(self):
            return [self.max_hp,self.hp,self.armor,self.weapons,self.current_weapon,self.active_items]