import pygame
class Ship():
    def __init__(self, screen):
        """initial ship and set the starting position"""
        self.screen = screen

        #load ship bmp and get the rectangle
        self.image = pygame.image.load('images/YYF.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #put the ship in the central bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom 

        #initial move action
        self.move_right = False
        self.move_left = False

    def blitme(self):
        """draw ship in given position"""
        if self.move_right:
            self.rect.centerx+=1
            if self.rect.right > self.screen_rect.right:
                self.rect.right = self.screen_rect.right
        elif self.move_left:
            self.rect.centerx-=1
            if self.rect.left < self.screen_rect.left:
                self.rect.left = self.screen_rect.left

        self.screen.blit(self.image, self.rect)
