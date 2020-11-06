from abc import ABCMeta, abstractmethod


class IRenderable():
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_sprite(self):
        """getting sprite of ..."""
