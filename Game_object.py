import abc


class Game_object(ABC):
    _id: int

    def get_id(self) -> int:
        return self._id
