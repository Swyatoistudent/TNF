import Item
from Hero import Hero

class PassiveItem (Item):
    def __init__(self, ammo_mod: int, damage_mod: int, hp_mod: int):
        self.__max_ammo_mod = ammo_mod
        self.__damage_mod = damage_mod
        self.__max_hp_mod = hp_mod

    def effect(self):
        Hero.max_hp +=self.__max_hp_mod
        Hero.max_ammo_mod += self.__max_ammo_mod
        Hero.damage_mod += self.__damage_mod






    @property
    def max_ammo_mod(self):
        return self.__max_ammo_mod
    @max_ammo_mod.setter
    def max_ammo_mod(self, new_ammo_mod: int):
        if isinstance(new_ammo_mod, int):
            self.__max_ammo_mod = new_ammo_mod
        else:
            raise ValueError(f'Can\'t create ammo modifier from type {type(new_ammo_mod)}')

    @property
    def damage_mod(self):
        return self.__damage_mod

    @damage_mod.setter
    def damage_mod(self, new_damage_mod: int):
        if isinstance(new_damage_mod, int):
            self.__damage_mod = new_damage_mod
        else:
            raise ValueError(f'Can\'t create ammo modifier from type {type(new_damage_mod)}')
    @property
    def max_hp_mod(self):
        return self.__max_hp_mod

    @max_hp_mod.setter
    def max_hp_mod(self, new_max_hp_mod: int):
        if isinstance(new_max_hp_mod, int):
            self.__damage_mod = new_max_hp_mod
        else:
            raise ValueError(f'Can\'t create ammo modifier from type {type(new_max_hp_mod)}')
