import pygame
import choicemenu
import sys
SCREEN_HEIGHT = 560

SCREEN_WIDTH = 1000
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                     pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
Background = pygame.image.load("IMG/start.png")

def StartMenu():
    run = True
    Background = pygame.surface

    while run:
        

        SCREEN.blit(pygame.image.load("IMG/start.png"), (0, 0))
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                choicemenu.mainmenu()

StartMenu()