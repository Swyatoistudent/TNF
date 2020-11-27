import Item

class ActiveItem (Item):
    def __init__(self, cooldown: int, atack_id: int ):
        self.__cooldown = cooldown
        self.__atack_id = atack_id

    @property
    def cooldown(self):
        return self.__cooldown
    @cooldown.setter
    def cooldown(self, new_cooldown: int):
        if isinstance(new_cooldown, int):
            self.__cooldown = new_cooldown
        else:
            raise ValueError(f'Can\'t create cooldown from type {type(new_cooldown)}')
