import sys
import pygame
from pygame.sprite import Group
from setting import Setting
from ship import Ship
import game_functions as gf
from bullet import Bullet


def run_game():
    #initial game and make a screen target
    pygame.init()
    setting = Setting()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    ship = Ship(setting, screen)
    bullets = Group()
    pygame.display.set_caption(setting.caption)

    #begin main loop
    while True:
        #watch keyboard and mouse
        gf.check_events(ship, bullets, setting, screen)

        ship.update_position()
        bullets.update()

        #refresh screen
        gf.update_screen(screen, setting, ship, bullets)
       
run_game()



