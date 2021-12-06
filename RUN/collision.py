import pygame
import os

pygame.init()

SCREEN_HEIGHT = 560
SCREEN_WIDTH = 1000
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]
BG01 = pygame.image.load(os.path.join("Assets/Other", "background.jpg"))
BG02 = BG01.copy()

tree = [pygame.image.load('Assets/Cactus/LargeCactus1.png')]
fire = [pygame.image.load('Assets/Bird/Bird1.png')]
<<<<<<< HEAD
=======

>>>>>>> 9581436b20ce6439d5787de08ca653838228f3e3


class Fireball:
    fire_x = SCREEN_WIDTH
class Dino:
    X_POS = 460
    Y_POS = 400
    Y_POS_DUCK = 340
    JUMP_VEL = 8

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 1
            Dino.Y_POS = 200
            
        if self.jump_vel < - 8:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL
            Dino.Y_POS = 400

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
    
def GameOver():
    font = pygame.font.Font('NanumGothic.ttf', 30)
    GAMEOVER = font.render("GAME OVER", True, (255,255,255))
    SCREEN.blit(GAMEOVER, (400, 250))

def main():
    global X_pos
    run = True
    clock = pygame.time.Clock()
    player = Dino()
    BG01_x = 0
    BG02_x = SCREEN_WIDTH

    # tree
    imgTree = pygame.image.load('Assets/Cactus/LargeCactus1.png')
    tree_x = SCREEN_WIDTH
    tree_x3 = SCREEN_WIDTH
    tree_y = 200
    tree_y3 = 200
    # fire
    imgfire = pygame.image.load('Assets/Bird/Bird1.png')
    fire_x = SCREEN_WIDTH
    fire_x3 = SCREEN_WIDTH
    fire_y = 200
    fire_y3 = 200

    def back(BG, x, y):
        global SCREEN, BG01
        SCREEN.blit(BG01, (x, y))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        BG01_x -= 40
        BG02_x -= 40

        if BG01_x == -SCREEN_WIDTH:
            BG01_x = SCREEN_WIDTH
        if BG02_x == -SCREEN_WIDTH:
            BG02_x = SCREEN_WIDTH

        back(BG01, BG01_x, 0)
        back(BG02, BG02_x, 0)

        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        # tree move
        tree_x -= 12.0
        if tree_x <= 0:
            tree_x = SCREEN_WIDTH
        if tree_x == Dino.X_POS and Dino.Y_POS == tree_y:
            tree_x = SCREEN_WIDTH

        
        tree_x3 -= 2.0
        if tree_x3 <= 0:
            tree_x3 = SCREEN_WIDTH
        if tree_x3 == Dino.X_POS and Dino.Y_POS == tree_y3:
            tree_x3 = SCREEN_WIDTH

        # fire move
        fire_x -= 6.0
        if fire_x <= 0:
            fire_x = SCREEN_WIDTH
        if fire_x == Dino.X_POS and Dino.Y_POS == fire_y:
            GameOver()
            pygame.display.flip()
            pygame.time.delay(20000)
            pygame.quit()
            exit()


        
        fire_x3 -= 4.0
        if fire_x3 <= 0:
            fire_x3 = SCREEN_WIDTH
        if fire_x3 == Dino.X_POS and Dino.Y_POS == fire_y3:
            GameOver()
            pygame.display.flip()
            pygame.time.delay(20000)
            pygame.quit()
            exit()


        SCREEN.blit(imgTree, (tree_x, tree_y))
        SCREEN.blit(imgTree, (tree_x3, tree_y3))
        SCREEN.blit(imgfire, (fire_x, fire_y))
        SCREEN.blit(imgfire, (fire_x3, fire_y3))




        clock.tick(30)
        pygame.display.update()


main()