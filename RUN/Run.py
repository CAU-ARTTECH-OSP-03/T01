import pygame

pygame.init()

SCREEN_H = 560
SCREEN_W = 1000
SCREEN = pygame.display.set_mode((SCREEN_W,SCREEN_H))

BG01 = pygame.image.load("IMG/background.jpg")
BG02 = BG01.copy()

clock = pygame.time.Clock()


class MeltingSnowman(pygame.sprite.Sprite):

    def __init__(self, position):

        super(MeltingSnowman, self).__init__()
        size = (100, 100)

        images = [(pygame.image.load('IMG/DinoRun1.png')),
                  (pygame.image.load('IMG/DinoRun2.png')),
                  (pygame.image.load('IMG/DinoJump.png')),
                  (pygame.image.load('IMG/DinoDuck1.png')),
                  (pygame.image.load('IMG/DinoDuck2.png'))]

        self.rect = pygame.Rect(position, size)
        self.images = [pygame.transform.scale(image, size) for image in images]

        self.index = 0
        self.image = images[self.index]

        self.animation_time = 1
        self.current_time = 0

    def update(self, mt):
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


def GameOver():
    font = pygame.font.Font('NanumGothic.ttf', 30)
    GAMEOVER = font.render("GAME OVER", True, (255,255,255))
    SCREEN.blit(GAMEOVER, (400, 250))

def Background(BG, x, y):
    global SCREEN, BG01
    SCREEN.blit(BG01, (x, y))

def main():

    player = MeltingSnowman(position=(80, 419))
    all_sprites = pygame.sprite.Group(player)

    BG01_x = 0
    BG02_x = SCREEN_W

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        mt = clock.tick(100) / 1000

        all_sprites.update(mt)
        all_sprites.draw(SCREEN)
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
