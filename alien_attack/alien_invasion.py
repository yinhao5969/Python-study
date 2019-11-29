import sys
import pygame
def run_game():
    #initial game and make a screen target
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Alien Invasion')
    #backgroud color
    bg_color = (240, 240, 240)
    #begin main loop
    while True:
        #watch keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #screen fill
        screen.fill(bg_color)
        #make drawed screen show
        pygame.display.flip()

run_game()



