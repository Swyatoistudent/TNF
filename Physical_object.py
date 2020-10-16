from typing import Any

import Game_object
import Collision


# game_objects_data = { id: { 'type': 'Physical_object', ....}, ....}

class Physical_object(Game_object):

    def __init__(self, id: int, position: [float, float]):
        if game_objects_data[id]['type'] != 'Physical_object':
            pass
            # raise ObjectTypeException
        self._id = id
        self._position = position
        self._size = game_objects_data[id]['size']
        self._collision = game_objects_data[id]['collision']

    # def get_id(self) -> int:
    #     return self._id

    def on_collide(self, collided: Physical_object, direction: int):
        if self._collision.get_damage() > 0 and isinstance(collided, Moveble_object):
            collided.damaged(self._collision.get_damage())
        temp = self._collision.get_collision_effect()
        if temp is not None:
            temp(collided, direction)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        if isinstance(new_position, [float, float]):
            self._position = new_position
        else:
            raise ValueError(f'Can\'t create position from type {type(new_position)}')

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if isinstance(new_size, int):
            self._size = new_size
        else:
            raise ValueError(f'Can\'t create size from type {type(new_size)}')
