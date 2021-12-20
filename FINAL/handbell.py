import sys
import pygame
import random
import time
import choicemenu

# 게임 화면 크기
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 560
pygame.init()

# 색상
GRAY = (150, 150, 150)
BLACK = (0, 0, 0)

# 소스 디렉토리

DIRBEATS = 'FINAL/IMG/'

# 기본 변수
SCORE = 0
BEAT_COUNT = 103

# bground
bground_img = pygame.image.load('FINAL/IMG/bellbg.png')
bground = pygame.transform.scale(bground_img, (1000, 560))
endingbg = pygame.image.load('FINAL/IMG/bellending.png')

# music
music = pygame.mixer.Sound('FINAL/wav/backmusic.wav')  # 배경음악
do = pygame.mixer.Sound('FINAL/wav/do.wav')  # 핸드벨
re = pygame.mixer.Sound('FINAL/wav/re.wav')
mi = pygame.mixer.Sound('FINAL/wav/mi.wav')
pa = pygame.mixer.Sound('FINAL/wav/pa.wav')
sol = pygame.mixer.Sound('FINAL/wav/sol.wav')
la = pygame.mixer.Sound('FINAL/wav/la.wav')
si = pygame.mixer.Sound('FINAL/wav/si.wav')
ddo = pygame.mixer.Sound('FINAL/wav/ddo.wav')

# time.sleep(3)  # 시간지연 3초
# music.play()  # 배경음악 1회실행

# beat오브젝트를 저장할 리스트
BEATS = []


class Beat:
    beat_image = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png']

    def __init__(self, x=0, y=0, dx=0, dy=0):
        self.image = ''
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rect = ''

    def load_beat(self, p=""):
        if p == "p":
            # 플레이어
            self.image = pygame.image.load(DIRBEATS + "player.png")
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

        else:
            # 비트 40개의 이미지중에서 랜덤으로 선택한다.
            self.image = pygame.image.load(DIRBEATS + random.choice(self.beat_image))
            self.rect = self.image.get_rect()

            beatwidth = 100
            beatheight = 100

            self.image = pygame.transform.scale(self.image, (beatwidth, beatheight))
            self.rect.width = beatwidth
            self.rect.height = beatheight

            # 생성 위치
            self.rect.x = self.x
            self.rect.y = self.y

    def draw_beat(self):
        SCREEN.blit(self.image, [self.rect.x, self.rect.y])

    # x 좌표 이동 - 플레이어의 움직임

    def move_x(self):
        self.rect.x = self.dx

    # y 좌표 이동 - 비트 y 움직임

    def move_y(self):
        self.rect.y += self.dy

    # 비트 충돌 감지
    # distance : 오른쪽, 왼쪽, 아래쪽, 위쪽 이미지의 간격 설정

    def check_collision(self, car, distance=0):
        if (self.rect.top + distance < car.rect.bottom) and (car.rect.top < self.rect.bottom - distance) and (
                self.rect.left + distance < car.rect.right) and (car.rect.left < self.rect.right - distance):
            return True
        else:
            return False

def GameOver():
    font = pygame.font.Font('NanumGothic.ttf', 30)
    GAMEOVER = font.render("GAME OVER", True, (255, 255, 255))
    SCREEN.blit(GAMEOVER, (400, 250))

def handbell1():
    global SCREEN, BEAT_COUNT, WINDOW_WIDTH, WINDOW_HEIGHT, SCORE
    
    time.sleep(3)  # 시간지연 3초
    music.play()  # 배경음악 1회실행
    # pygame 초기화 및 스크린 생성

    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),
                                     pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
    pygame.display.set_caption("DO NOT CRY HAND BELL")
    # 투명 아이콘은 32 x 32 로 해야 적용 됨
    #windowicon = pygame.image.load(DIRBEATS + '1.png').convert_alpha()
    #pygame.display.set_icon(windowicon)

    # bellimage
    bell1_img = pygame.image.load('FINAL/IMG/doredf.png')
    bell2_img = pygame.image.load('FINAL/IMG/doreleft.png')
    bell3_img = pygame.image.load('FINAL/IMG/doreright.png')

    bell4_img = pygame.image.load('FINAL/IMG/mipadf.png')
    bell5_img = pygame.image.load('FINAL/IMG/mipaleft.png')
    bell6_img = pygame.image.load('FINAL/IMG/miparight.png')

    bell7_img = pygame.image.load('FINAL/IMG/solradf.png')
    bell8_img = pygame.image.load('FINAL/IMG/solraleft.png')
    bell9_img = pygame.image.load('FINAL/IMG/solraright.png')

    bell10_img = pygame.image.load('FINAL/IMG/sidodf.png')
    bell11_img = pygame.image.load('FINAL/IMG/sidoleft.png')
    bell12_img = pygame.image.load('FINAL/IMG/sidoright.png')

    clock = pygame.time.Clock()

    # player class 지정
    player = Beat(50, 450, 0, 0)
    player.load_beat("p")

    # beat 좌표 class에 추가
    beat = Beat(300, 0, 0, 16)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(400, -100, 0, 16)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -200, 0, 16)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -300, 0, 16)
    beat.load_beat()
    BEATS.append(beat)
    # 미파솔솔
    beat = Beat(600, -500, 0, 15)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(700, -600, 0, 15)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(800, -700, 0, 15)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(800, -800, 0, 15)
    beat.load_beat()
    BEATS.append(beat)
    # 라시도도
    beat = Beat(300, -1000, 0, 13)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(400, -1100, 0, 13)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -1200, 0, 13)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -1300, 0, 13)
    beat.load_beat()
    BEATS.append(beat)
    # 미파솔솔
    beat = Beat(600, -1500, 0, 13)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -1550, 0, 13)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(400, -1650, 0, 13)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(400, -1750, 0, 13)
    beat.load_beat()
    BEATS.append(beat)
    # 라솔파파
    beat = Beat(300, -1950, 0, 11.5)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -2050, 0, 11.5)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(100, -2150, 0, 11.4)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(300, -2250, 0, 11.4)
    beat.load_beat()
    BEATS.append(beat)
    # 미솔도미
    beat = Beat(200, -2400, 0, 11.4)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(400, -2500, 0, 11.3)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(200, -2700, 0, 11)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(100, -2800, 0, 11)
    beat.load_beat()
    BEATS.append(beat)
    # 레파레도-----------------------
    beat = Beat(300, -3800, 0, 11)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(400, -3900, 0, 11)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -4000, 0, 11)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -4100, 0, 11)
    beat.load_beat()
    BEATS.append(beat)
    # 미파솔솔
    beat = Beat(600, -4300, 0, 11)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(700, -4400, 0, 11)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(800, -4500, 0, 11)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(800, -4600, 0, 11)
    beat.load_beat()
    BEATS.append(beat)
    # 라시도도
    beat = Beat(300, -4800, 0, 11)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(400, -4900, 0, 11)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -5000, 0, 11)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -5100, 0, 11)
    beat.load_beat()
    BEATS.append(beat)
    # 미파솔솔
    beat = Beat(600, -5300, 0, 10.8)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -5400, 0, 10.8)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(400, -5500, 0, 10.8)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(400, -5600, 0, 10.7)
    beat.load_beat()
    BEATS.append(beat)
    # 라솔파파-
    beat = Beat(300, -5800, 0, 10.008)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -5950, 0, 10.008)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(100, -6050, 0, 10.008)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(300, -6150, 0, 10.008)
    beat.load_beat()
    BEATS.append(beat)
    # 미솔도미
    beat = Beat(200, -6350, 0, 10.008)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(400, -6450, 0, 10.008)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(200, -6650, 0, 10.008)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(100, -6750, 0, 10.008)
    beat.load_beat()
    BEATS.append(beat)
    # 레파레도------------------------
    beat = Beat(300, -7200, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(400, -7300, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -7400, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -7500, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    # 미파솔솔
    beat = Beat(600, -7700, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(700, -7790, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(800, -7890, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(800, -7990, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    # 라시도도
    beat = Beat(300, -8190, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(400, -8290, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -8390, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -8490, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    # 미파솔솔
    beat = Beat(600, -8650, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -8790, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(400, -8890, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(400, -8990, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    # 라솔파파
    beat = Beat(300, -9190, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -9290, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(100, -9390, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(300, -9490, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    # 미솔도미
    beat = Beat(200, -9690, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(400, -9850, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(200, -9950, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(100, -10050, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    # 레파레도---------------------
    beat = Beat(300, -10800, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(400, -10900, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -11000, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -11100, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    # 미파솔솔
    beat = Beat(600, -11280, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(700, -11380, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(800, -11480, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(800, -11580, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    # 라시도도
    beat = Beat(300, -11680, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(400, -11780, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -11880, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -11980, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    # 미파솔솔
    beat = Beat(600, -12180, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -12280, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(400, -12390, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(400, -12490, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    # 라솔파파
    beat = Beat(300, -12690, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -12790, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(100, -12890, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(300, -12990, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    # 미솔도미
    beat = Beat(200, -13190, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(400, -13290, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(700, -13450, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(800, -13550, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    # 레파시도--------------------------
    beat = Beat(800, -13600, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(800, -13700, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(800, -13800, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(800, -13900, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    # 도도도도
    beat = Beat(800, -14000, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(500, -14100, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    beat = Beat(100, -14200, 0, 10)
    beat.load_beat()
    BEATS.append(beat)
    # 솔도

    playing = True

    while playing:
        SCREEN.blit(bground, (0, 0))
        SCREEN.blit(bell1_img, (200, 270))
        SCREEN.blit(bell4_img, (280, 270))
        SCREEN.blit(bell7_img, (460, 280))
        SCREEN.blit(bell10_img, (560, 280))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    do.play()
                    player.dx = 100
                    SCREEN.blit(bell2_img, (200, 270))
                elif event.key == pygame.K_s:
                    re.play()
                    player.dx = 200
                    SCREEN.blit(bell3_img, (200, 270))
                elif event.key == pygame.K_d:
                    mi.play()
                    player.dx = 300
                    SCREEN.blit(bell5_img, (280, 270))
                elif event.key == pygame.K_f:
                    pa.play()
                    player.dx = 400
                    SCREEN.blit(bell6_img, (280, 270))
                elif event.key == pygame.K_g:
                    sol.play()
                    player.dx = 500
                    SCREEN.blit(bell8_img, (460, 280))
                elif event.key == pygame.K_h:
                    la.play()
                    player.dx = 600
                    SCREEN.blit(bell9_img, (460, 280))
                elif event.key == pygame.K_j:
                    si.play()
                    player.dx = 700
                    SCREEN.blit(bell11_img, (560, 280))
                elif event.key == pygame.K_k:
                    ddo.play()
                    player.dx = 800
                    SCREEN.blit(bell12_img, (560, 280))
                elif event.key == pygame.K_q:
                    pygame.mixer.music.stop()
                    SCREEN.blit(endingbg, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    choicemenu.mainmenu()

        player.load_beat("p")
        player.move_x()
        player.draw_beat()
        end = pygame.mixer.music.set_endevent

        for i in range(BEAT_COUNT):
            BEATS[i].draw_beat()
            BEATS[i].rect.y += BEATS[i].dy
            if BEATS[102].rect.y == 560:
                if SCORE >= 3000:
                    SCREEN.blit(endingbg, (0, 0))
                    pygame.mixer.music.stop()
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    choicemenu.mainmenu()
                if SCORE < 3000:
                    SCREEN.blit(endingbg, (100, 100))
                    pygame.mixer.music.stop()
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    choicemenu.mainmenu()


        for i in range(BEAT_COUNT):
            if player.check_collision(BEATS[i], 0):
                # 부딪쳤을 경우 빠르게 내려가기
                if player.rect.x == BEATS[i].rect.x:
                    BEATS[i].rect.y += 40
                    SCORE += 10

        #print(SCORE)


        # 글씨
        font_01 = pygame.font.SysFont("FixedSsy", 30, True, False)
        text_score = font_01.render("Score : " + str(SCORE), True, (255,255,255))
        SCREEN.blit(text_score, [15, 15])
        pygame.display.flip()

        # 초당 프레임 설정
        clock.tick(25)


if __name__ == '__main__':
    handbell1()