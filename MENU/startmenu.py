import pygame
pygame.init()

SCREEN_HEIGHT = 560
SCREEN_WIDTH = 1000
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

Background = pygame.image.load("IMG/MenuBackground.png")

def StartMenu():
    run = True
    Background = pygame.surface

    while run:
        font = pygame.font.Font('NanumGothic.ttf', 30)
        text = font.render("Press any Key to Start", True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        SCREEN.blit(pygame.image.load("IMG/MenuBackground.png"), (0, 0))
        SCREEN.blit(text, textRect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                pygame.quit()

StartMenu()