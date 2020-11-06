from abc import ABCMeta, abstractmethod


class IDamageable():
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_damage(self, damage):
        """getting damage"""
