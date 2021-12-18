import pygame
import time
import random
import sys
from rungame import rungame1
from ddrgame import ddrgame1
from handbell import handbell1
pygame.init()

white = (255,255,255)

titleImg = pygame.image.load("./IMG/Menu_name.png")
runstartImg = pygame.image.load("./IMG/Snowman_menu.png")
bellstartImg = pygame.image.load("./IMG/Handbell_menu.png")
ddrstartImg = pygame.image.load("./IMG/Santa_menu.png")
quitImg = pygame.image.load("./IMG/Quit.png")
clickStartImg = pygame.image.load("./IMG/Santa03.png")
clickQuitImg = pygame.image.load("./IMG/Quit.png")

display_width = 1000
display_height = 560
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Merry Winter Story")

clock = pygame.time.Clock()


class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act, (x_act, y_act))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            gameDisplay.blit(img_in, (x, y))


def quitgame():
    pygame.quit()
    sys.exit()


def mainmenu():

    display_width = 1000
    display_height = 560
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.flip()
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        titletext = gameDisplay.blit(titleImg, (470, 100))
        rungameButton = Button(runstartImg, 140, 260, 100, 50, clickStartImg, 180, 260, rungame1)
        bellgameButton = Button(bellstartImg, 420, 260, 100, 50, clickStartImg, 460, 260, handbell1)
        ddrgameButton = Button(ddrstartImg, 700, 260, 100, 50, clickStartImg, 740, 260, ddrgame1)
        quitButton = Button(quitImg, 850, 400, 60, 20, clickQuitImg, 840, 400, quitgame)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    mainmenu()