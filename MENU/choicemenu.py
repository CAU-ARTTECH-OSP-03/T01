import pygame
import time
import random

pygame.init()

white = (255, 255, 255)

titleImg = pygame.image.load("IMG/index_3.png")
runstartImg = pygame.image.load("IMG/RUN.png")
bellstartImg = pygame.image.load("IMG/BELL.png")
ddrstartImg = pygame.image.load("IMG/DDR.png")
quitImg = pygame.image.load("IMG/Fireball.png")
clickStartImg = pygame.image.load("IMG/sun.png")
clickQuitImg = pygame.image.load("IMG/wind.png")


display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Merry Winter Story")

clock = pygame.time.Clock()



class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act,(x_act, y_act))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            gameDisplay.blit(img_in,(x,y))

def quitgame():
    pygame.quit()
    sys.exit()


def mainmenu():
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        
        titletext = gameDisplay.blit(titleImg, (470,100))
        rungameButton = Button(runstartImg,140,260,100,50,clickStartImg,180,260,main)
        bellgameButton = Button(bellstartImg,420,260,100,50,clickStartImg,460,260,main)
        ddrgameButton = Button(ddrstartImg,700,260,100,50,clickStartImg,740,260,main)
        quitButton = Button(quitImg,850,400,60,20,clickQuitImg,840,400,quitgame)
        pygame.display.update()
        clock.tick(15)



SCREEN_H = 560
SCREEN_W = 1000
SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))

BG01 = pygame.image.load("IMG/background.jpg")
BG02 = BG01.copy()
clock = pygame.time.Clock()


class MeltingSnowman(pygame.sprite.Sprite):
    SnowMan_X = 100
    SnowMan_Y = 419
    position = (SnowMan_X, SnowMan_Y)
    JUMP_VEL = 8

    def __init__(self, position):

        SnowMan_X = 100
        SnowMan_Y = 419

        position = (SnowMan_X, SnowMan_Y)

        self.SM_run = True
        self.SM_jump = False
        self.jump_vel = self.JUMP_VEL

        super(MeltingSnowman, self).__init__()
        size = (100, 100)

        images = [(pygame.image.load('IMG/index_0.png')),
                  (pygame.image.load('IMG/index_1.png')),
                  (pygame.image.load('IMG/index_2.png')),
                  (pygame.image.load('IMG/index_3.png')),
                  (pygame.image.load('IMG/index_4.png'))]

        self.rect = pygame.Rect(position, size)
        self.rect.x = self.SnowMan_X
        self.rect.y = self.SnowMan_Y
        self.images = [pygame.transform.scale(image, size) for image in images]

        self.index = 0
        self.image = images[self.index]

        self.animation_time = 1
        self.current_time = 0

    def update(self, userInput):
        self.image = self.images[self.index]
        userInput = pygame.key.get_pressed()
        mt = clock.tick(100) / 1000

        if self.SM_run:
            self.run(mt)
        if self.SM_jump:
            self.jump()

        if userInput[pygame.K_UP] and not self.SM_jump:
            self.SM_run = False
            self.SM_jump = True
        elif not (self.SM_jump or userInput[pygame.K_DOWN]):
            self.SM_run = True
            self.SM_jump = False

    def run(self, mt):
        self.current_time += mt

        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index += 1
            if self.index == len(self.images):
                GameOver()
                pygame.display.flip()
                pygame.time.delay(2000)
                mainmenu()

    def jump(self):
        if self.SM_jump:
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= 1
            MeltingSnowman.SnowMan_Y = 300

        if self.jump_vel < - 8:
            self.SM_jump = False
            self.jump_vel = self.JUMP_VEL
            MeltingSnowman.SnowMan_Y = 419

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))


class IceBall:

    def __init__(self, x, y, speed, player, a, b):
        self.Ice_x = x
        self.Ice_y = y
        self.speed = speed
        self.player = player
        self.x_rt = a
        self.time_diff = b
        self.imgIce = pygame.image.load('IMG/iceball.png')

    def Fly_over(self):
        self.Ice_x -= self.speed

        if self.Ice_x <= 0:
            self.Ice_x = SCREEN_W + self.x_rt
        if self.Ice_x == self.player.SnowMan_X and self.player.SnowMan_Y == self.Ice_y:
            self.Ice_x = SCREEN_W + self.time_diff
            self.player.index -= 1
            if self.player.index == -1:
                self.player.index = 0

    def draw(self, SCREEN):
        SCREEN.blit(self.imgIce, (self.Ice_x, self.Ice_y))


class FireBall:

    def __init__(self, x, y, speed, a):
        self.Fire_x = x
        self.Fire_y = y
        self.speed = speed
        self.x_rt = a
        self.imgFire = pygame.image.load('IMG/fireball.png')

    def Fly_over(self):
        self.Fire_x -= self.speed
        if self.Fire_x <= 0:
            self.Fire_x = SCREEN_W + self.x_rt
        if self.Fire_x == MeltingSnowman.SnowMan_X and MeltingSnowman.SnowMan_Y == self.Fire_y:
            GameOver()
            pygame.display.flip()
            pygame.time.delay(2000)
            mainmenu()

    def draw(self, SCREEN):
        SCREEN.blit(self.imgFire, (self.Fire_x, self.Fire_y))


class Obstacle:

    def __init__(self, x, y, speed, a):
        self.Obstacle_x = x
        self.Obstacle_y = y
        self.speed = speed
        self.x_rt = a
        self.imgObstacle = pygame.image.load('IMG/obstacle.png')

    def Appear(self):
        self.Obstacle_x -= self.speed
        if self.Obstacle_x <= 0:
            self.Obstacle_x = SCREEN_W + self.x_rt
        if self.Obstacle_x == MeltingSnowman.SnowMan_X and MeltingSnowman.SnowMan_Y == self.Obstacle_y:
            GameOver()
            pygame.display.flip()
            pygame.time.delay(2000)
            mainmenu()

    def draw(self, SCREEN):
        SCREEN.blit(self.imgObstacle, (self.Obstacle_x, self.Obstacle_y))


class Cloud:
    def __init__(self, x, y, speed):
        self.Cloud_x = x
        self.Cloud_y = y
        self.speed = speed
        self.imagecld = pygame.image.load("IMG/Cloud.png")
        self.width = SCREEN_W

    def update(self):
        self.Cloud_x -= self.speed
        if self.Cloud_x < -self.width:
            self.Cloud_x = SCREEN_W + random.randint(2500, 3000)
            self.Cloud_y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.imagecld, (self.Cloud_x, self.Cloud_y))


class Sun:
    def __init__(self, x, y, speed):
        self.Sun_x = x
        self.Sun_y = y
        self.speed = speed
        self.imagesun = pygame.image.load("IMG/Sun.png")
        self.width = SCREEN_W

    def update(self):
        self.Sun_x -= self.speed
        if self.Sun_x == 100:
            GameClear()
            pygame.display.flip()
            pygame.time.delay(3000)
            mainmenu()

    def draw(self, SCREEN):
        SCREEN.blit(self.imagesun, (self.Sun_x, self.Sun_y))


class Wind:
    def __init__(self, x, y, speed):
        self.Wind_x = x
        self.Wind_y = y
        self.speed = speed
        self.imagewind = pygame.image.load("IMG/Wind.png")
        self.width = SCREEN_W

    def update(self):
        self.Wind_x -= self.speed
        if self.Wind_x < -self.width:
            self.Wind_x = SCREEN_W + random.randint(2500, 3000)
            self.Wind_y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.imagewind, (self.Wind_x, self.Wind_y))


def GameOver():
    font = pygame.font.Font('NanumGothic.ttf', 30)
    GAMEOVER = font.render("GAME OVER", True, (255, 255, 255))
    SCREEN.blit(GAMEOVER, (400, 250))


def GameClear():
    font = pygame.font.Font('NanumGothic.ttf', 30)
    GAMECLEAR = font.render("GAME CLEAR", True, (255, 255, 255))
    SCREEN.blit(GAMECLEAR, (400, 250))


def Background(BG, x, y):
    global SCREEN, BG01
    SCREEN.blit(BG01, (x, y))


def main():
    MeltingSnowman.SnowMan_X = 100
    MeltingSnowman.SnowMan_Y = 419
    player = MeltingSnowman(position=(100, 419))
    all_sprites = pygame.sprite.Group(player)
    Iceball01 = IceBall(SCREEN_W, 300, 20, player, 0, 500)
    Fireball01 = FireBall(SCREEN_W, 300, 10, 300)
    Fireball02 = FireBall(SCREEN_W, 300, 24, 300)
    Obstacle01 = Obstacle(SCREEN_W, 419, 20, 100)
    Obstacle02 = Obstacle(SCREEN_W, 419, 25, 600)

    Cloud01 = Cloud(SCREEN_W, 100, 20)
    Sun01 = Sun(SCREEN_W, 70, 1)
    Wind01 = Wind(SCREEN_W, 100, 60)
    BG01_x = 0
    BG02_x = SCREEN_W

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        userInput = pygame.key.get_pressed()
        mt = clock.tick(100) / 1000

        player.draw(SCREEN)
        
        all_sprites.update(mt)
        all_sprites.update(userInput)
        all_sprites.draw(SCREEN)

        Fireball01.Fly_over()
        Fireball01.draw(SCREEN)

        Fireball02.Fly_over()
        Fireball02.draw(SCREEN)

        Iceball01.Fly_over()
        Iceball01.draw(SCREEN)

        Obstacle01.Appear()
        Obstacle01.draw(SCREEN)

        Obstacle02.Appear()
        Obstacle02.draw(SCREEN)

        Cloud01.update()
        Cloud01.draw(SCREEN)

        Sun01.update()
        Sun01.draw(SCREEN)

        Wind01.update()
        Wind01.draw(SCREEN)
        pygame.display.update()

        BG01_x -= 4
        BG02_x -= 4

        if BG01_x == -SCREEN_W:
            BG01_x = SCREEN_W
        if BG02_x == -SCREEN_W:
            BG02_x = SCREEN_W

        Background(BG01, BG01_x, 0)
        Background(BG02, BG02_x, 0)
        clock.tick(50)





mainmenu()
