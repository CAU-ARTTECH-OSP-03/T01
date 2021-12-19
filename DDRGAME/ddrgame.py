import pygame
import time
import random



pygame.init()
screen_width = 360
screen_height = 720

blockImage = [pygame.image.load("st1.png"),
              pygame.image.load("st2.png"),
              pygame.image.load("st3.png"),
              pygame.image.load("st4.png")]

playerImage = [pygame.image.load("뚝1.png"),
               pygame.image.load("뚝2.png"),
               pygame.image.load("뚝3.png"),
               pygame.image.load("뚝4.png")]

barImage = [pygame.image.load("바1.png"),
            pygame.image.load("바2.png"),
            pygame.image.load("바3.png"),
            pygame.image.load("바4.png")]

backImage = [pygame.image.load("배경/ddrbg1.jpg"),
             pygame.image.load("배경/ddrbg2.jpg"),
             pygame.image.load("배경/ddrbg3.png")]
imgBar = pygame.image.load("bar.png")
background = pygame.image.load("배경.gif")



gamePad = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption('DDR GAME')
music = pygame.mixer.music.load("jinglebell.mp3")
pygame.mixer.music.play(1)
pygame.mixer.music.get_pos()




pygame.init()


white = (255, 255, 255)

titleImg = pygame.image.load("C:\Git\T01\MENU\IMG\index_3.png")
runstartImg = pygame.image.load("C:\Git\T01\MENU\IMG\RUN.png")
bellstartImg = pygame.image.load("C:\Git\T01\MENU\IMG\BELL.png")
ddrstartImg = pygame.image.load("C:\Git\T01\MENU\IMG\DDR.png")
quitImg = pygame.image.load("C:\Git\T01\MENU\IMG\Fireball.png")
clickStartImg = pygame.image.load("C:\Git\T01\MENU\IMG\sun.png")
clickQuitImg = pygame.image.load("C:\Git\T01\MENU\IMG\wind.png")




pygame.display.set_caption("Merry Winter Story")
pygame.display.flip()
clock = pygame.time.Clock()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))



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


def mainmenu(self):
    menu = True

    titleImg = pygame.image.load("C:\Git\T01\MENU\IMG\Menu_name.png")
    runstartImg = pygame.image.load("C:\Git\T01\FINAL\IMG\Snowman_menu.png")
    bellstartImg = pygame.image.load("C:\Git\T01\FINAL\IMG\Handbell_menu.png")
    ddrstartImg = pygame.image.load("C:\Git\T01\FINAL\IMG\Santa_menu.png")
    quitImg = pygame.image.load("C:\Git\T01\FINAL\IMG\Quit.png")
    clickStartImg = pygame.image.load("C:\Git\T01\FINAL\IMG\sun.png")
    clickQuitImg = pygame.image.load("C:\Git\T01\FINAL\IMG\Quit.png")


    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        
        titletext = gameDisplay.blit(titleImg, (470,100))
        rungameButton = Button(runstartImg,140,260,100,50,clickStartImg,180,260,rungame.main)
        bellgameButton = Button(bellstartImg,420,260,100,50,clickStartImg,460,260,rungame.main)
        ddrgameButton = Button(ddrstartImg,700,260,100,50,clickStartImg,740,260,rungame.main)
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




if __name__ == '__main__':
    mainmenu()




def Cleargame():
    gamePad = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font('NanumGothic.ttf', 30)
    GAMECLEAR = font.render("GAME CLEAR", True, (255, 255, 255))
    gamePad.blit(GAMECLEAR, (85, 280))

def gameover():
    gamePad = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font('NanumGothic.ttf', 30)
    GAMEOVER = font.render("GAME OVER", True, (255, 255, 255))
    gamePad.blit(GAMEOVER, (85, 280))

def perfect():
    gamePad = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font('NanumGothic.ttf', 30)
    perfect = font.render("perfect", True, (255, 255, 255))
    gamePad.blit(perfect, (130, 280))

def Miss():
    gamePad = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font('NanumGothic.ttf', 30)
    Miss = font.render("Miss", True, (255, 255, 255))
    gamePad.blit(Miss, (145, 280))
class snow:
    gamePad = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    pygame.display.set_caption('DDR GAME')
    music = pygame.mixer.music.load("jinglebell.mp3")
    pygame.mixer.music.play(1)
    pygame.mixer.music.get_pos()
    def __init__(self, x, y, speed):
        self.snow_x = x
        self.snow_y = y
        self.speed = speed
        self.imgsnow = pygame.image.load("bar.png")

    def fallingsnow(self):
        self.snow_y += self.speed
        if self.snow_y == 100:
            Cleargame()
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
            exit()

    def draw(self):
        gamePad = pygame.display.set_mode((screen_width, screen_height))
        gamePad.blit(self.imgsnow, (self.snow_x, self.snow_y))


class bar:
    def __init__(self, x, y, i):
        self.bar_x = x
        self.bar_y = y
        self.imgBar = barImage[i]

    def draw(self):
        gamePad = pygame.display.set_mode((screen_width, screen_height))
        gamePad.blit(self.imgBar, (self.bar_x, self.bar_y))


class player:
    def __init__(self, x, y, i):
        self.player_x = x
        self.player_y = y
        self.imgPlayer = playerImage[i]

    def draw(self):
        gamePad = pygame.display.set_mode((screen_width, screen_height))
        gamePad.blit(self.imgPlayer, (self.player_x, self.player_y))


class Block:
    def __init__(self, x, y, speed, i):
        pygame.sprite.Sprite.__init__(self)
        self.block_x = x
        self.block_y = y
        self.speed = speed
        self.imgBlock = blockImage[i]

    def Falling(self):
        self.block_y += self.speed
        if self.block_y >= screen_height:
            self.block_y = 0

    def draw(self):
        SCREEN.blit(self.imgBlock, (self.block_x, self.block_y))

    def die(self):
        for block in blockImage:
            blockImage.remove(block)


def Background(BG, x, y):
    global background
    gamePad = pygame.display.set_mode((screen_width, screen_height))
    gamePad.blit(background, (x, y))



def main():
    clock = pygame.time.Clock()
    pygame.display.set_caption('DDR GAME')
    music = pygame.mixer.music.load("jinglebell.mp3")
    pygame.mixer.music.play(1)
    pygame.mixer.music.get_pos()
    Bar01 = bar(0, 640, 0)
    Bar02 = bar(90, 640, 1)
    Bar03 = bar(180, 640, 2)
    Bar04 = bar(270, 640, 3)
    Block01 = Block(0, 0, 5, 0)
    Block02 = Block(90, 0, 4.5, 1)
    Block03 = Block(180, 0, 3.5, 2)
    Block04 = Block(270, 0, 5, 3)
    Player01 = player(0, 650, 0)
    Player02 = player(90, 650, 1)
    Player03 = player(180, 650, 2)
    Player04 = player(270, 650, 3)
    snow01 = snow(500, -1900, 0.5)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    Bar01.bar_y = 635
                elif event.key == pygame.K_s:
                    Bar02.bar_y = 635
                elif event.key == pygame.K_k:
                    Bar03.bar_y = 635
                elif event.key == pygame.K_l:
                    Bar04.bar_y = 635

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    Bar01.bar_y = 640
                if event.key == pygame.K_s:
                    Bar02.bar_y = 640
                if event.key == pygame.K_k:
                    Bar03.bar_y = 640
                if event.key == pygame.K_l:
                    Bar04.bar_y = 640

        bl01_rect = blockImage[0].get_rect()
        bl01_rect.left = Block01.block_x
        bl01_rect.top = Block01.block_y
        bl01_rect.bottom = Block01.block_y + 40

        bl02_rect = blockImage[1].get_rect()
        bl02_rect.left = Block02.block_x
        bl02_rect.top = Block02.block_y
        bl02_rect.bottom = Block02.block_y + 40

        bl03_rect = blockImage[2].get_rect()
        bl03_rect.left = Block03.block_x
        bl03_rect.top = Block03.block_y
        bl03_rect.bottom = Block03.block_y + 40

        bl04_rect = blockImage[3].get_rect()
        bl04_rect.left = Block04.block_x
        bl04_rect.top = Block04.block_y
        bl04_rect.bottom = Block04.block_y + 40

        Bar01_rect = imgBar.get_rect()
        Bar01_rect.left = Bar01.bar_x
        Bar01_rect.top = Bar01.bar_y
        Bar01_rect.bottom = Bar01.bar_y + 20

        Bar02_rect = imgBar.get_rect()
        Bar02_rect.left = Bar02.bar_x
        Bar02_rect.top = Bar02.bar_y
        Bar02_rect.bottom = Bar02.bar_y + 20

        Bar03_rect = imgBar.get_rect()
        Bar03_rect.left = Bar03.bar_x
        Bar03_rect.top = Bar03.bar_y
        Bar03_rect.bottom = Bar03.bar_y + 20

        Bar04_rect = imgBar.get_rect()
        Bar04_rect.left = Bar04.bar_x
        Bar04_rect.top = Bar04.bar_y
        Bar04_rect.bottom = Bar04.bar_y + 20

        pressed = pygame.key.get_pressed()

        if bl01_rect.colliderect(Bar01_rect):
            if bl01_rect.bottom > Bar01_rect.bottom > bl01_rect.top:

                if pressed[pygame.K_a]:
                    perfect()

                else:
                    gameover()
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    mainmenu()

        if bl02_rect.colliderect(Bar02_rect):
            if bl02_rect.bottom > Bar02_rect.bottom > bl02_rect.top:
                if pressed[pygame.K_s]:
                        perfect()
                else:
                    gameover()
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    mainmenu()
        if bl03_rect.colliderect(Bar03_rect):
            if bl03_rect.bottom > Bar03_rect.bottom > bl03_rect.top:
                if pressed[pygame.K_k]:
                        perfect()
                else:
                    gameover()
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    #mainmenu()
        if bl04_rect.colliderect(Bar04_rect):
            if bl01_rect.bottom > Bar04_rect.bottom > bl04_rect.top:
                if pressed[pygame.K_l]:
                        perfect()
                else:
                    gameover()
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    #mainmenu()

        # if (Block02.block_y) == (Bar02.bar_y):
        #     print("판정")
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_LEFT:
        #             print("판정")

        # if (Block01.block_y + 40)

        Block01.draw()
        Block01.Falling()
        Block02.draw()
        Block02.Falling()
        Block03.draw()
        Block03.Falling()
        Block04.draw()
        Block04.Falling()
        Player01.draw()
        Player02.draw()
        Player03.draw()
        Player04.draw()
        Bar01.draw()
        Bar02.draw()
        Bar03.draw()
        Bar04.draw()
        snow01.draw()
        snow01.fallingsnow()
        pygame.display.update()

        Background(background, 0, 0)
        clock.tick(50)


main()