import pygame


class Screen:
    def __init__(self, level, surf):
        self.__static = []
        self.__dynamic = []
        background = None
        self.on_load(level)
        self.__surf = surf

    def on_load(self, level):
        pass

    def render(self):
        for obj in self.__dynamic:
            self.__surf.blit(obj.animation.get_animation_move(obj.velocity_vector), obj.position)
