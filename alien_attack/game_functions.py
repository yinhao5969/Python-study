import sys
import pygame
from bullet import Bullet

def check_events(ship, bullets , ai_settings, screen):
    #watch keyboard and mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.move_right = True
            elif event.key == pygame.K_LEFT:                
                ship.move_left = True
            elif event.key == pygame.K_SPACE:
                fire(ship, bullets , ai_settings, screen)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.move_right = False
            elif event.key == pygame.K_LEFT:                
                ship.move_left = False

def fire(ship, bullets , ai_settings, screen):
    if len(bullets) < ai_settings.bullet_max :
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(screen, setting, ship, bullets):
    #screen fill
    screen.fill(setting.bg_color)

    #draw ship
    ship.blitme()

    #draw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #make drawed screen show       
    pygame.display.flip()
