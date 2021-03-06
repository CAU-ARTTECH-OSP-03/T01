{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a4599c78",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  },
  "pycharm": {
   "stem_cell": {
    "cell_type": "raw",
    "source": [
     "import sys\n",
     "import pygame\n",
     "import random\n",
     "import time\n",
     "\n",
     "# 게임 화면 크기\n",
     "WINDOW_WIDTH = 1000\n",
     "WINDOW_HEIGHT = 560\n",
     "pygame.init()\n",
     "\n",
     "# 색상\n",
     "GRAY = (150, 150, 150)\n",
     "BLACK = (0, 0, 0)\n",
     "\n",
     "# 소스 디렉토리\n",
     "\n",
     "DIRBEATS = 'C:/Users/sunsum/Documents/opensource/teamproject/beat/'\n",
     "\n",
     "# 기본 변수\n",
     "SCORE = 0\n",
     "BEAT_COUNT = 103\n",
     "\n",
     "# bground\n",
     "bground_img = pygame.image.load('bellbg.png')\n",
     "bground = pygame.transform.scale(bground_img, (1000, 560))\n",
     "endingbg = pygame.image.load('bell_ending.png')\n",
     "\n",
     "# music\n",
     "music = pygame.mixer.Sound('backmusic.wav')  # 배경음악\n",
     "do = pygame.mixer.Sound('do.wav')  # 핸드벨\n",
     "re = pygame.mixer.Sound('re.wav')\n",
     "mi = pygame.mixer.Sound('mi.wav')\n",
     "pa = pygame.mixer.Sound('pa.wav')\n",
     "sol = pygame.mixer.Sound('sol.wav')\n",
     "la = pygame.mixer.Sound('la.wav')\n",
     "si = pygame.mixer.Sound('si.wav')\n",
     "ddo = pygame.mixer.Sound('ddo.wav')\n",
     "\n",
     "time.sleep(3)  # 시간지연 3초\n",
     "music.play()  # 배경음악 1회실행\n",
     "\n",
     "# beat오브젝트를 저장할 리스트\n",
     "BEATS = []\n",
     "\n",
     "\n",
     "\n",
     "class Beat:\n",
     "    beat_image = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png']\n",
     "\n",
     "    def __init__(self, x=0, y=0, dx=0, dy=0):\n",
     "        self.image = ''\n",
     "        self.x = x\n",
     "        self.y = y\n",
     "        self.dx = dx\n",
     "        self.dy = dy\n",
     "        self.rect = ''\n",
     "\n",
     "    def load_beat(self, p=\"\"):\n",
     "        if p == \"p\":\n",
     "            # 플레이어\n",
     "            self.image = pygame.image.load(DIRBEATS + \"player.png\")\n",
     "            self.image = pygame.transform.scale(self.image, (100, 100))\n",
     "            self.rect = self.image.get_rect()\n",
     "            self.rect.x = self.x\n",
     "            self.rect.y = self.y\n",
     "\n",
     "        else:\n",
     "            # 비트 40개의 이미지중에서 랜덤으로 선택한다. \n",
     "            self.image = pygame.image.load(DIRBEATS + random.choice(self.beat_image))\n",
     "            self.rect = self.image.get_rect()\n",
     "\n",
     "            beatwidth = 100\n",
     "            beatheight = 100\n",
     "\n",
     "            self.image = pygame.transform.scale(self.image, (beatwidth, beatheight))\n",
     "            self.rect.width = beatwidth\n",
     "            self.rect.height = beatheight\n",
     "\n",
     "            # 생성 위치 \n",
     "            self.rect.x = self.x\n",
     "            self.rect.y = self.y\n",
     "\n",
     "\n",
     "\n",
     "    def draw_beat(self):\n",
     "        SCREEN.blit(self.image, [self.rect.x, self.rect.y])\n",
     "\n",
     "    # x 좌표 이동 - 플레이어의 움직임\n",
     "\n",
     "    def move_x(self):\n",
     "        self.rect.x = self.dx\n",
     "\n",
     "    # y 좌표 이동 - 비트 y 움직임\n",
     "\n",
     "    def move_y(self):\n",
     "        self.rect.y += self.dy\n",
     "\n",
     "    # 비트 충돌 감지\n",
     "    # distance : 오른쪽, 왼쪽, 아래쪽, 위쪽 이미지의 간격 설정\n",
     "\n",
     "    def check_collision(self, car, distance=0):\n",
     "        if (self.rect.top + distance < car.rect.bottom) and (car.rect.top < self.rect.bottom - distance) and (\n",
     "                self.rect.left + distance < car.rect.right) and (car.rect.left < self.rect.right - distance):\n",
     "            return True\n",
     "        else:\n",
     "            return False\n",
     "\n",
     "\n",
     "def main():\n",
     "    global SCREEN, BEAT_COUNT, WINDOW_WIDTH, WINDOW_HEIGHT, SCORE\n",
     "\n",
     "    # pygame 초기화 및 스크린 생성\n",
     "\n",
     "    pygame.init()\n",
     "    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),\n",
     "                                     pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)\n",
     "    pygame.display.set_caption(\"DO NOT CRY HAND BELL\")\n",
     "    # 투명 아이콘은 32 x 32 로 해야 적용 됨\n",
     "    windowicon = pygame.image.load(DIRBEATS + '1.png').convert_alpha()\n",
     "    pygame.display.set_icon(windowicon)\n",
     "    \n",
     "    # bellimage\n",
     "    bell1_img = pygame.image.load('doredf.png')\n",
     "    bell2_img = pygame.image.load('doreleft.png')\n",
     "    bell3_img = pygame.image.load('doreright.png')\n",
     "    \n",
     "    bell4_img = pygame.image.load('mipadf.png')\n",
     "    bell5_img = pygame.image.load('mipaleft.png')\n",
     "    bell6_img = pygame.image.load('miparight.png')\n",
     "    \n",
     "    bell7_img = pygame.image.load('solradf.png')\n",
     "    bell8_img = pygame.image.load('solraleft.png')\n",
     "    bell9_img = pygame.image.load('solraright.png')\n",
     "    \n",
     "    bell10_img = pygame.image.load('sidodf.png') \n",
     "    bell11_img = pygame.image.load('sidoleft.png')\n",
     "    bell12_img = pygame.image.load('sidoright.png')\n",
     "    \n",
     "\n",
     "    clock = pygame.time.Clock()\n",
     "\n",
     "    # player class 지정\n",
     "    player = Beat(50, 450, 0, 0)\n",
     "    player.load_beat(\"p\")\n",
     "\n",
     "    # beat 좌표 class에 추가\n",
     "    beat = Beat(300, 0, 0, 16)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(400, -100, 0, 16)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -200, 0, 16)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -300, 0, 16)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 미파솔솔\n",
     "    beat = Beat(600, -500, 0, 15)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(700, -600, 0, 15)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(800, -700, 0, 15)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(800, -800, 0, 15)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 라시도도\n",
     "    beat = Beat(300, -1000, 0, 13)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(400, -1100, 0, 13)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -1200, 0, 13)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -1300, 0, 13)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 미파솔솔\n",
     "    beat = Beat(600, -1500, 0, 13)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -1550, 0, 13)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(400, -1650, 0, 13)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(400, -1750, 0, 13)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 라솔파파\n",
     "    beat = Beat(300, -1950, 0, 11.5)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -2050, 0, 11.5)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(100, -2150, 0, 11.4)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(300, -2250, 0, 11.4)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 미솔도미\n",
     "    beat = Beat(200, -2400, 0, 11.4)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(400, -2500, 0, 11.3)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(200, -2700, 0, 11)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(100, -2800, 0, 11)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 레파레도-----------------------\n",
     "    beat = Beat(300, -3800, 0, 11)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(400, -3900, 0, 11)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -4000, 0, 11)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -4100, 0, 11)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 미파솔솔\n",
     "    beat = Beat(600, -4300, 0, 11)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(700, -4400, 0, 11)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(800, -4500, 0, 11)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(800, -4600, 0, 11)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 라시도도\n",
     "    beat = Beat(300, -4800, 0, 11)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(400, -4900, 0, 11)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -5000, 0, 11)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -5100, 0, 11)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 미파솔솔\n",
     "    beat = Beat(600, -5300, 0, 10.8)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -5400, 0, 10.8)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(400, -5500, 0, 10.8)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(400, -5600, 0, 10.7)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 라솔파파-\n",
     "    beat = Beat(300, -5800, 0, 10.008)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -5950, 0, 10.008)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(100, -6050, 0, 10.008)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(300, -6150, 0, 10.008)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 미솔도미\n",
     "    beat = Beat(200, -6350, 0, 10.008)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(400, -6450, 0, 10.008)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(200, -6650, 0, 10.008)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(100, -6750, 0, 10.008)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 레파레도------------------------\n",
     "    beat = Beat(300, -7200, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(400, -7300, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -7400, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -7500, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 미파솔솔\n",
     "    beat = Beat(600, -7700, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(700, -7790, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(800, -7890, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(800, -7990, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 라시도도\n",
     "    beat = Beat(300, -8190, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(400, -8290, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -8390, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -8490, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 미파솔솔\n",
     "    beat = Beat(600, -8650, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -8790, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(400, -8890, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(400, -8990, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 라솔파파\n",
     "    beat = Beat(300, -9190, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -9290, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(100, -9390, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(300, -9490, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 미솔도미\n",
     "    beat = Beat(200, -9690, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(400, -9850, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(200, -9950, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(100, -10050, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 레파레도---------------------\n",
     "    beat = Beat(300, -10800, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(400, -10900, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -11000, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -11100, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 미파솔솔\n",
     "    beat = Beat(600, -11280, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(700, -11380, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(800, -11480, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(800, -11580, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 라시도도\n",
     "    beat = Beat(300, -11680, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(400, -11780, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -11880, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -11980, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 미파솔솔\n",
     "    beat = Beat(600, -12180, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -12280, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(400, -12390, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(400, -12490, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 라솔파파\n",
     "    beat = Beat(300, -12690, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -12790, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(100, -12890, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(300, -12990, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 미솔도미\n",
     "    beat = Beat(200, -13190, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(400, -13290, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(700, -13450, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(800, -13550, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    #레파시도--------------------------\n",
     "    beat = Beat(800, -13600, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(800, -13700, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(800, -13800, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(800, -13900, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 도도도도\n",
     "    beat = Beat(800, -14000, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(500, -14100, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    beat = Beat(100, -14200, 0, 10)\n",
     "    beat.load_beat()\n",
     "    BEATS.append(beat)\n",
     "    # 솔도  \n",
     "    \n",
     "    playing = True\n",
     "    \n",
     "    while playing:\n",
     "        SCREEN.fill(GRAY)\n",
     "        SCREEN.blit(bground, (0, 0))\n",
     "        SCREEN.blit(bell1_img, (200, 270))\n",
     "        SCREEN.blit(bell4_img, (280, 270))\n",
     "        SCREEN.blit(bell7_img, (460, 280))\n",
     "        SCREEN.blit(bell10_img, (560, 280))\n",
     "\n",
     "        for event in pygame.event.get():\n",
     "            if event.type == pygame.QUIT:\n",
     "                playing = False\n",
     "                pygame.quit()\n",
     "                sys.exit()\n",
     "\n",
     "            if event.type == pygame.KEYDOWN:\n",
     "                if event.key == pygame.K_a:\n",
     "                    do.play()\n",
     "                    player.dx = 100\n",
     "                    SCREEN.blit(bell2_img, (200, 270))\n",
     "                elif event.key == pygame.K_s:\n",
     "                    re.play()\n",
     "                    player.dx = 200\n",
     "                    SCREEN.blit(bell3_img, (200, 270))            \n",
     "                elif event.key == pygame.K_d:\n",
     "                    mi.play()\n",
     "                    player.dx = 300\n",
     "                    SCREEN.blit(bell5_img, (280, 270))                     \n",
     "                elif event.key == pygame.K_f:\n",
     "                    pa.play()\n",
     "                    player.dx = 400\n",
     "                    SCREEN.blit(bell6_img, (280, 270))                     \n",
     "                elif event.key == pygame.K_g:\n",
     "                    sol.play()\n",
     "                    player.dx = 500\n",
     "                    SCREEN.blit(bell8_img, (460, 280)) \n",
     "                elif event.key == pygame.K_h:\n",
     "                    la.play()\n",
     "                    player.dx = 600\n",
     "                    SCREEN.blit(bell9_img, (460, 280))             \n",
     "                elif event.key == pygame.K_j:\n",
     "                    si.play()\n",
     "                    player.dx = 700\n",
     "                    SCREEN.blit(bell11_img, (560, 280))                     \n",
     "                elif event.key == pygame.K_k:\n",
     "                    ddo.play()\n",
     "                    player.dx = 800\n",
     "                    SCREEN.blit(bell12_img, (560, 280))                     \n",
     "\n",
     "        player.load_beat(\"p\")\n",
     "        player.move_x()\n",
     "        player.draw_beat()\n",
     "        for i in range(BEAT_COUNT):\n",
     "            BEATS[i].draw_beat()\n",
     "            BEATS[i].rect.y += BEATS[i].dy\n",
     "            if i == BEAT_COUNT:\n",
     "                break\n",
     "\n",
     "        for i in range(BEAT_COUNT):\n",
     "            if player.check_collision(BEATS[i], 0):\n",
     "                # 부딪쳤을 경우 빠르게 내려가기\n",
     "                if player.rect.x == BEATS[i].rect.x:\n",
     "                    BEATS[i].rect.y += 40\n",
     "                    SCORE += 10\n",
     "\n",
     "        print(SCORE)\n",
     "        if SCORE >= 3760:\n",
     "            SCREEN.blit(endingbg, (0, 0))\n",
     "\n",
     "        #글씨\n",
     "        font_01 = pygame.font.SysFont(\"FixedSsy\", 30, True, False)\n",
     "        text_score = font_01.render(\"Score : \" + str(SCORE), True, BLACK)\n",
     "        SCREEN.blit(text_score, [15, 15])\n",
     "        pygame.display.flip()\n",
     "        \n",
     "        # 초당 프레임 설정\n",
     "        clock.tick(25)\n",
     "\n",
     "\n",
     "if __name__ == '__main__':\n",
     "    main()\n",
     "\n",
     "\n",
     "\n"
    ],
    "metadata": {
     "collapsed": false
    }
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}