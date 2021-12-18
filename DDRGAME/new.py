import pygame

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


def Cleargame():
    font = pygame.font.Font('NanumGothic.ttf', 30)
    GAMECLEAR = font.render("GAME CLEAR", True, (255, 255, 255))
    gamePad.blit(GAMECLEAR, (85, 280))

def gameover():
    font = pygame.font.Font('NanumGothic.ttf', 30)
    GAMEOVER = font.render("GAME OVER", True, (255, 255, 255))
    gamePad.blit(GAMEOVER, (85, 280))

def perfect():
    font = pygame.font.Font('NanumGothic.ttf', 30)
    perfect = font.render("perfect", True, (255, 255, 255))
    gamePad.blit(perfect, (130, 280))

def Miss():
    font = pygame.font.Font('NanumGothic.ttf', 30)
    Miss = font.render("Miss", True, (255, 255, 255))
    gamePad.blit(Miss, (145, 280))
class snow:
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
        gamePad.blit(self.imgsnow, (self.snow_x, self.snow_y))


class bar:
    def __init__(self, x, y, i):
        self.bar_x = x
        self.bar_y = y
        self.imgBar = barImage[i]

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
        gamePad.blit(self.imgBlock, (self.block_x, self.block_y))

    def die(self):
        for block in blockImage:
            blockImage.remove(block)


def Background(BG, x, y):
    global gamePad, background
    gamePad.blit(background, (x, y))



def main():
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
                    #mainmenu()
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