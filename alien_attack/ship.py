import pygame
class Ship():
    def __init__(self, ai_settings, screen):
        """initial ship and set the starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        #load ship bmp and get the rectangle
        self.image = pygame.image.load('images/YYF.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #put the ship in the central bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        #initial move action
        self.move_right = False
        self.move_left = False

    def update_position(self):
        if self.move_right:
            self.center+=self.ai_settings.ship_speed_factor
            self.rect.centerx = self.center
            if self.rect.right > self.screen_rect.right:
                self.rect.right = self.screen_rect.right
                self.center = self.rect.centerx
        elif self.move_left:
            self.center-=self.ai_settings.ship_speed_factor
            self.rect.centerx = self.center
            if self.rect.left < self.screen_rect.left:
                self.rect.left = self.screen_rect.left
                self.center = self.rect.centerx

    def blitme(self):
        """draw ship in given position"""
        

        self.screen.blit(self.image, self.rect)
