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

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)