import sys
import pygame
from bullet import Bullet
from alien import Alien

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

def update_screen(screen, setting, ship, bullets, aliens):
    #screen fill
    screen.fill(setting.bg_color)

    #draw ship
    ship.blitme()

    #draw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #draw aliens
    for alien in aliens.sprites():
        alien.draw_alien()

    #make drawed screen show       
    pygame.display.flip()

def creat_fleet(ai_settings, screen, aliens):
    alien = Alien(ai_settings, screen)
    alien_cnt = int((ai_settings.screen_width - alien.rect.width * 2) / (alien.rect.width * 2))
    for sequence in range(alien_cnt):
        alien = Alien(ai_settings, screen)
        alien.rect.x = alien.rect.width + alien.rect.width * 2 * sequence
        alien.center_x = alien.rect.centerx
        alien.center_y = alien.rect.centery
        aliens.add(alien)

def kill(aliens, bullets):
    collsions = pygame.sprite.groupcollide(bullets, aliens, True, True)

def check_fleet_get_edge(aliens):
    for alien in aliens.sprites():
        screen_rect = alien.screen.get_rect()
        if alien.rect.right > screen_rect.right:
            return True
        elif alien.rect.left < screen_rect.left:
            return True
        else:
            continue
    
    return False

def get_fleet_direction(aliens, ai_settings):
    if check_fleet_get_edge(aliens):
        ai_settings.fleet_move_directon = -ai_settings.fleet_move_directon
        
        for alien in aliens.sprites():
            #move in vertical dirction
            alien.center_y += alien.ai_settings.fleet_approach_speed_factor
            alien.rect.centery = alien.center_y


