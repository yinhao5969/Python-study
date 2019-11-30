import sys
import pygame

from setting import Setting
from ship import Ship

def run_game():
    #initial game and make a screen target
    pygame.init()
    setting = Setting()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    ship = Ship(screen)
    pygame.display.set_caption(setting.caption)

    #begin main loop
    while True:
        #watch keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #screen fill
        screen.fill(setting.bg_color)
        #make drawed screen show        
        ship.blitme()
        pygame.display.flip()
run_game()



