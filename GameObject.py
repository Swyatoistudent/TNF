import abc
from Loader import game_objects_data


class GameObject(abc.ABC):
    _id: int

    def get_id(self) -> int:
        return self._id
