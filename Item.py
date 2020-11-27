import abc
import GameObject

class Item(abc.ABC,GameObject):
    _rarity: int

    def get_rarity(self) -> int:
        return self._rarity
