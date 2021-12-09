import pygame
import sys
import random


pygame.init()

screen_width = 360
screen_height = 720
WHITE = (0,0,0)
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

background_image = pygame.image.load('./배경/back.png')

block_a = pygame.image.load('block1.png')
block_a_size = block_a.get_rect().size
block_a_width = block_a_size[0]
block_a_height = block_a_size[1]

block_a_x_pos = 0
block_a_y_pos = 0
block_a_speed = 1

running=True
while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    block_a_y_pos += block_a_speed
    if block_a_y_pos > screen_height:
        block_a_y_pos = 0


    screen.blit(background_image,(0,0))
    screen.blit(block_a,(block_a_x_pos, block_a_y_pos))
    pygame.display.update()
pygame.quit()

