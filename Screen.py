import pygame


class Screen:
    def __init__(self, level, surf):
        self.__static = []
        self.__dynamic = []
        self.__background = None
        self.on_load(level)
        self.__surf = surf

    def on_load(self, level):
        pass

    def render(self):
        self.__surf.blit(self.__background,)
        for obj in self.__static:
            self.__surf.blits(zip(obj.animation.get_animation_move(obj.velocity_vector), obj.position))
        for obj in self.__dynamic:
            self.__surf.blits(zip(obj.animation.get_animation_move(obj.velocity_vector), obj.position))
