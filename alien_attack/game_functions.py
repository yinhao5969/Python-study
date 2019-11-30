import sys

import pygame

def check_events(ship):
    #watch keyboard and mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.move_right = True
            elif event.key == pygame.K_LEFT:                
                ship.move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.move_right = False
            elif event.key == pygame.K_LEFT:                
                ship.move_left = False

def update_screen(screen, setting, ship):
    #screen fill
    screen.fill(setting.bg_color)
     
    #draw ship
    ship.blitme()

    #make drawed screen show       
    pygame.display.flip()
