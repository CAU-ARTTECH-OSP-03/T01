import pygame
import sys
import random


pygame.init()

screen_width = 360
screen_height = 720
WHITE = (0,0,0)
blockImage = ['block1.png','block2.png','block3.png','block4.png']


def drawObject(obj, x, y):
    global gamePad, background, clock, playerA, playerS, playerK, playerL, block
    gamePad.blit(obj,(x,y))

def initGame():
    global gamePad, background, clock, playerA, playerS, playerK, playerL, block
    pygame.init()
    gamePad = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('DDR GAME')
    background = pygame.image.load("./배경/back.png")
    playerA = pygame.image.load("./배경/A.png")
    playerS = pygame.image.load("./배경/S1.png")
    playerK = pygame.image.load("./배경/K1.png")
    playerL = pygame.image.load("./배경/L1.png")
    #block = pygame.image.load("./배경/block1.png")
    clock = pygame.time.Clock()

#게임 이벤트 시작
def runGame():
    global gamePad, clock, background, playerA, playerS, playerK, playerL, block

    pygame.mixer.music.load("just fine.mp3")
    pygame.mixer.music.play(1)
    # #블럭크기
    # blockSize = block.get_rect().size
    # blockWidth = blockSize[0]
    # blockHeight = blockSize[1]
    #
    # #블럭 초기 위치(x,y)
    # x = screen_width * 0
    # y = screen_height *0
    # blockX = 0

    #player A 크기
    playerASize = playerA.get_rect().size
    playerAWidth = playerASize[0]
    playerAHeight = playerASize[1]

    #player A 초기위치(X,Y)
    x_a = screen_width * 0
    y_a = screen_height - playerAHeight
    playerX_A = 0

    # player S 크기
    playerS_Size = playerS.get_rect().size
    playerSWidth = playerS_Size[0]
    playerSHeight = playerS_Size[1]


    # player S 초기위치(X,Y)
    x_s = screen_width - 90
    y_s = screen_height - playerSHeight
    playerX_S = 0

    # player K 크기
    playerKSize = playerK.get_rect().size
    playerKWidth = playerKSize[0]
    playerKHeight = playerKSize[1]


    # player K 초기위치(X,Y)
    x_k = screen_width - 180
    y_k = screen_height - playerKHeight
    playerX_K = 0

    # player L 크기
    playerSize = playerL.get_rect().size
    playerLWidth = playerSize[0]
    playerLHeight = playerSize[1]

    # player L 초기위치(X,Y)
    x_l = screen_width - 270
    y_l = screen_height - playerLHeight
    playerX_L = 0

    #BLOCK 생성 후 떨어지기
    block = pygame.image.load(random.choice(blockImage))
    blockSize = block.get_rect().size
    blockWidth = blockSize[0]
    blockHeight = blockSize[1]
    #BLOCK 랜덤생성
    xx = [0, 90, 180, 270]
    #blockX = random.randrange(0, random.choice(xx))
    blockX = random.choice(xx)
    blockY = 0
    blockSpeed = 3


    running = True
    while running:

        blockY += blockSpeed
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                y_a -= 2
            if event.key == pygame.K_RIGHT:
                y_s -= 2
            if event.key == pygame.K_UP:
                y_l -= 2
            if event.key == pygame.K_DOWN:
                y_k -=2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                y_a = screen_height - playerAHeight
            if event.key == pygame.K_RIGHT:
                y_s = screen_height - playerSHeight
            if event.key == pygame.K_UP:
                y_l = screen_height - playerLHeight
            if event.key == pygame.K_DOWN:
                y_k = screen_height - playerKHeight
                # if y_a < -3:
                #     y_a += 3


        if blockY > screen_height:
            block = pygame.image.load(random.choice(blockImage))
            blockSize = block.get_rect().size
            blockWidth = blockSize[0]
            blockHeight = blockSize[1]
            blockX = random.choice(xx)
            blockY = 0

        # 버튼 반응코드
        y_a += playerX_A
        if y_a < 0:
            y_a = 0
        elif y_a > screen_height - playerAHeight:
            y_a = screen_height - playerAHeight

        y_s += playerX_S
        if y_s < 0:
            y_s = 0
        elif y_s > screen_height - playerSHeight:
            y_s = screen_height - playerSHeight

        y_k += playerX_K
        if y_k < 0:
            y = 0
        elif y_k > screen_height - playerKHeight:
            y_k = screen_height - playerKHeight

        y_k += playerX_L
        if y_l < 0:
            y = 0
        elif y_l > screen_height - playerLHeight:
            y_l = screen_height -playerLHeight

        drawObject(background, 0, 0)#배경화면 그리기
        #drawObject(block, x, y)
        drawObject(block, blockX, blockY)
        drawObject(playerA, x_a, y_a)
        drawObject(playerS, x_s, y_s)
        drawObject(playerK, x_k, y_k)
        drawObject(playerL, x_l, y_l)
        pygame.display.update()# 게임화면 다시그림


initGame()
runGame()
pygame.quit()

