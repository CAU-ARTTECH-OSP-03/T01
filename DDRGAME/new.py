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
<<<<<<< HEAD
    def __init__(self, x, y, speed , i):
        self.block_x = x
        self.block_y = y
        self.speed = speed
        self.imgBlock = blockImage[i]

    def Falling(self):
        self.block_y += self.speed
        if self.block_y >= screen_height:
            self.block_y = 0

    def draw(self):
        gamePad.blit(self.imgBlock, (self.block_x, self.block_y))    

=======
    def __init__(self, x, y, i):
        self.block_x = x
        self.block_y = y
        self.imgBlock = blockImage[i]

>>>>>>> 85eed127509526c51457f88f287f703f206a32fb
def Background(BG, x, y):
    global gamePad, background
    gamePad.blit(background, (x, y))

def main():
    Bar01 = bar(0, 640)
    Bar02 = bar(90, 640)
    Bar03 = bar(180, 640)
    Bar04 = bar(270, 640)
<<<<<<< HEAD
    Block011 = Block(0,0,10,0)
    Block012 = Block(0,0,20,0)
    Block021 = Block(90,0,12,1)
    Block022 = Block(90,0,9,1)
    Block031 = Block(180,0,15,2)
    Block032 = Block(180,0,20,2)
    Block041 = Block(270,0,6,3)
    Block042 = Block(270,0,24,3)
=======
>>>>>>> 85eed127509526c51457f88f287f703f206a32fb
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
<<<<<<< HEAD
        Block011.draw()
        Block011.Falling()
        Block012.draw()
        Block012.Falling()
        Block021.draw()
        Block021.Falling()
        Block022.draw()
        Block022.Falling()
        Block031.draw()
        Block031.Falling()
        Block032.draw()
        Block032.Falling()
        Block041.draw()
        Block041.Falling()
        Block042.draw()
        Block042.Falling()
=======
>>>>>>> 85eed127509526c51457f88f287f703f206a32fb
        pygame.display.update()

        Background(background, 0, 0)
        clock.tick(50)

<<<<<<< HEAD
main()
=======
<<<<<<< HEAD
main()
=======
main()
>>>>>>> fbf124b8e2f3019f13e48e2984a9f3bb9d0301dc
>>>>>>> 85eed127509526c51457f88f287f703f206a32fb
