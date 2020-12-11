import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((1920, 1080))
menu = pygame_menu.Menu(1080, 1920, 'Welcome',
                        theme=pygame_menu.themes.THEME_DARK)

def start_the_game():
    pass

menu.add_button('Play', start_the_game)

menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)
