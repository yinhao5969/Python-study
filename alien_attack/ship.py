import pygame
class Ship():
    def __init__(self, screen):
        """initial ship and set the starting position"""
        self.screen = screen

        #load ship bmp and get the rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #put the ship in the central bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom 

    def blitme(self):
        """draw ship in given position"""
        self.screen.blit(self.image, self.rect)
