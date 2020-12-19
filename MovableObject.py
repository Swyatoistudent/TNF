from typing import List, Any

import PhysicalObject
import IRenderable
from loader import game_objects_data


class MovableObject(PhysicalObject):
    _velocity_vector: List[Any]

    def __init__(self, id: int, position: [float, float], type_name="MovableObject"):
        super(MovableObject, self).__init__(id, position, type_name=type_name)
        self._max_hp = game_objects_data[id]['max_hp']
        self._hp = self._max_hp
        self._speed = game_objects_data[id]['speed']
        self._velocity_vector = [0, 0]
        self.drop = game_objects_data[id]['drop']
        self.animation = game_objects_data[id]['animation']
        self._position = position

    def is_collided(self, collided: [PhysicalObject], direction: [int, int]):
        for coll in collided:
            coll.on_collide(self, coll, direction)

    def move(self, direction: [int, int]):
        if self._velocity_vector == [0, 0]:
            self._velocity_vector = direction
        else:
            self._velocity_vector = [self._velocity_vector[i] * 0.1
                                     + direction[i] * 0.9
                                     for i in range(2)]
        self._position = [self._position[i]
                          + self._speed * self._velocity_vector[i]
                          for i in range(2)]

    @property
    def hp(self):
        return self._hp

    @property
    def max_hp(self):
        return self._max_hp

    @property
    def velocity_vector(self):
        return self._velocity_vector
