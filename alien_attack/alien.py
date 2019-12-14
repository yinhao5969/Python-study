import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen  = screen
        self.ai_settings  = ai_settings

        #load alien bmp and get the rectangle
        self.image = pygame.image.load('images/virus.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.screen_rect = screen.get_rect()
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        #move in horizontal direction
        self.center_x += self.ai_settings.fleet_move_speed_factor * self.ai_settings.fleet_move_directon
        self.rect.centerx = self.center_x