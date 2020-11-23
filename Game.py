import pygame
import functools


def singleton(class_):
    instances = {}

    @functools.wraps(class_)
    def inner(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return inner


@singleton
class Game:
    FPS = 60

    def __init__(self, screen, hero, surf):
        self.__surf = surf
        self.__screen = screen
        self.__hero = hero
        self.__running = True
        self.__clock = pygame.time.Clock()

    def menu(self):
        pass

    def on_event(self, event):
        if event == pygame.K_ESCAPE:
            self.menu()
        if repr(event) in self.__hero.control.keys:
            self.__hero.control.keys[repr(event)]()

    def quit(self):
        pygame.quit()

    def run(self):
        while self.__running:
            self.__clock.tick(self.FPS)
            self.__screen.render(self.__surf)
            for event in pygame.event.get():
                self.on_event(event)
        self.quit()
