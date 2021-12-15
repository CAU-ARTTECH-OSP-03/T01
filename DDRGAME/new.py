import pygame

pygame.init()
screen_width = 360
screen_height = 720

blockImage = [pygame.image.load("block1.png"),
              pygame.image.load("block2.png"),
              pygame.image.load("block3.png"),
              pygame.image.load("block4.png")]

playerImage = [pygame.image.load("배경/A.png"),
               pygame.image.load("배경/S1.png"),
               pygame.image.load("배경/K1.png"),
               pygame.image.load("배경/L1.png")]

background = pygame.image.load("배경/back.png")

gamePad = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption('DDR GAME')
pygame.mixer.music.load("just fine.mp3")
pygame.mixer.music.play(1)

class bar:
    def __init__(self, x, y):
        self.bar_x = x
        self.bar_y = y
        self.imgBar = pygame.image.load("bar.png")

    def draw(self):
        gamePad.blit(self.imgBar, (self.bar_x, self.bar_y))

class player:
    def __init__(self, x, y, i):
        self.player_x = x
        self.player_y = y
        self.imgPlayer = playerImage[i]

    def draw(self):
        gamePad.blit(self.imgPlayer, (self.player_x, self.player_y))

class Block:
    def __init__(self, x, y, i):
        self.block_x = x
        self.block_y = y
        self.imgBlock = blockImage[i]

def Background(BG, x, y):
    global gamePad, background
    gamePad.blit(background, (x, y))

def main():
    Bar01 = bar(0, 640)
    Bar02 = bar(90, 640)
    Bar03 = bar(180, 640)
    Bar04 = bar(270, 640)
    Player01 = player(0, 670, 0)
    Player02 = player(90, 670, 1)
    Player03 = player(180, 670, 2)
    Player04 = player(270, 670, 3)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Bar01.bar_y = 635
            if event.key == pygame.K_RIGHT:
                Bar02.bar_y = 635
            if event.key == pygame.K_UP:
                Bar03.bar_y = 635
            if event.key == pygame.K_DOWN:
                Bar04.bar_y = 635

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                Bar01.bar_y = 640
            if event.key == pygame.K_RIGHT:
                Bar02.bar_y = 640
            if event.key == pygame.K_UP:
                Bar03.bar_y = 640
            if event.key == pygame.K_DOWN:
                Bar04.bar_y = 640

        Bar01.draw()
        Bar02.draw()
        Bar03.draw()
        Bar04.draw()
        Player01.draw()
        Player02.draw()
        Player03.draw()
        Player04.draw()
        pygame.display.update()

        Background(background, 0, 0)
        clock.tick(50)

<<<<<<< HEAD
main()
=======
main()
>>>>>>> fbf124b8e2f3019f13e48e2984a9f3bb9d0301dc
