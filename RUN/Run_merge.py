import pygame

pygame.init()

SCREEN_H = 560
SCREEN_W = 1000
SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))

BG01 = pygame.image.load("IMG/background.jpg")
BG02 = BG01.copy()

clock = pygame.time.Clock()


class MeltingSnowman(pygame.sprite.Sprite):
    SnowMan_X = 80
    SnowMan_Y = 419
    position = (SnowMan_X, SnowMan_Y)
    JUMP_VEL = 8

    def __init__(self, position):
        SnowMan_X = 80
        SnowMan_Y = 419
        position = (SnowMan_X, SnowMan_Y)

        self.SM_run = True
        self.SM_jump = False
        self.jump_vel = self.JUMP_VEL

        super(MeltingSnowman, self).__init__()
        size = (100, 100)

        images = [(pygame.image.load('IMG/DinoRun1.png')),
                  (pygame.image.load('IMG/DinoRun2.png')),
                  (pygame.image.load('IMG/DinoJump.png')),
                  (pygame.image.load('IMG/DinoDuck1.png')),
                  (pygame.image.load('IMG/DinoDuck2.png'))]

        self.rect = pygame.Rect(position, size)
        self.rect.x = self.SnowMan_X
        self.rect.y = self.SnowMan_Y
        self.images = [pygame.transform.scale(image, size) for image in images]

        self.index = 0
        self.image = images[self.index]

        self.animation_time = 1
        self.current_time = 0

    def update(self, userInput):
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
                pygame.quit()
                exit()

            self.image = self.images[min(self.index, len(self.images) - 1)]

    def jump(self):
        self.image = self.images[self.index]
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

    def __init__(self, x, y, speed):
        self.Ice_x = x
        self.Ice_y = y
        self.speed = speed

        self.imgIce = pygame.image.load('Assets/Cactus/LargeCactus1.png')
        self.ice_rect = self.imgIce.get_rect()
        self.ice_rect.x = self.Ice_x
        self.ice_rect.y = self.Ice_y

    def Fly_over(self):
        self.Ice_x -= self.speed
        if self.Ice_x <= 0:
            self.Ice_x = SCREEN_W
        if self.Ice_x == MeltingSnowman.SnowMan_X and MeltingSnowman.SnowMan_Y == self.Ice_y:
            self.Ice_x = SCREEN_W

    def draw(self, SCREEN):
        SCREEN.blit(self.imgIce, (self.Ice_x, self.Ice_y))

def GameOver():
    font = pygame.font.Font('NanumGothic.ttf', 30)
    GAMEOVER = font.render("GAME OVER", True, (255,255,255))
    SCREEN.blit(GAMEOVER, (400, 250))

def Background(BG, x, y):
    global SCREEN, BG01
    SCREEN.blit(BG01, (x, y))

def main():
    player = MeltingSnowman(position=(80, 419))
    Iceball01 = IceBall(SCREEN_W, 300, 10)
    all_sprites = pygame.sprite.Group(player)

    BG01_x = 0
    BG02_x = SCREEN_W

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        userInput = pygame.key.get_pressed()
        mt = clock.tick(100) / 1000

        all_sprites.update(mt)
        all_sprites.update(userInput)
        all_sprites.draw(SCREEN)
        pygame.display.update()

        Iceball01.Fly_over()
        Iceball01.draw(SCREEN)
        pygame.display.update()

        BG01_x -= 4; BG02_x -= 4

        if BG01_x == -SCREEN_W:
            BG01_x = SCREEN_W
        if BG02_x == -SCREEN_W:
            BG02_x = SCREEN_W

        Background(BG01, BG01_x, 0)
        Background(BG02, BG02_x, 0)

        clock.tick(30)


main()