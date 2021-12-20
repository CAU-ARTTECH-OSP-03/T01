import pygame
import time
import random
import sys
import rungame
import ddrgame
import handbell
pygame.init()

white = (255,255,255)

titleImg = pygame.image.load("FINAL/IMG/Menutitle.png")
runstartImg = pygame.image.load("FINAL/IMG/meltingsnowman.png")
bellstartImg = pygame.image.load("FINAL/IMG/Handbellringing.png")
ddrstartImg = pygame.image.load("FINAL/IMG/Santaddr.png")
quitImg = pygame.image.load("FINAL/IMG/Quit.png")
clickStartImg = pygame.image.load("FINAL/IMG/Santa03.png")
clickQuitImg = pygame.image.load("FINAL/IMG/Quit.png")

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

    
    menu = True
    while menu:
        print(pygame.event.get())
        for event in pygame.event.get():
            break
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        titletext = gameDisplay.blit(titleImg, (400, 100))
        rungameButton = Button(runstartImg, 120, 260, 100, 50, clickStartImg, 160, 260, rungame.rungame1)
        bellgameButton = Button(bellstartImg, 400, 260, 100, 50, clickStartImg, 440, 260, handbell.handbell1)
        ddrgameButton = Button(ddrstartImg, 680, 260, 100, 50, clickStartImg, 720, 260, ddrgame.ddrgame1)
        quitButton = Button(quitImg, 850, 400, 60, 20, clickQuitImg, 840, 400, quitgame)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    mainmenu()