#!/usr/bin/python

import sys
import pygame
from pygame.locals import *

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('PONG')
    pygame.key.set_repeat(10, 10)
    clock = pygame.time.Clock()
    black = (0, 0, 0)
    white = (255, 255, 255)
    left_pos = (40, 200)
    right_pos = (580, 200)

    # main loop
    while True:
        clock.tick(50) # limit to 50fps

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_UP and right_pos[1] > 0:
                    right_pos = (580, right_pos[1] - 2)
                elif event.key == K_DOWN and right_pos[1] < 400:
                    right_pos = (580, right_pos[1] + 2)
                elif event.key == K_q and left_pos[1] < 400:
                    left_pos = (40, left_pos[1] - 2)
                elif event.key == K_a and left_pos[1] < 400:
                    left_pos = (40, left_pos[1] + 2)

        screen.fill(black)
        pygame.draw.rect(screen, white, (left_pos[0], left_pos[1], 20, 80))
        pygame.draw.rect(screen, white, (right_pos[0], right_pos[1], 20, 80))
        pygame.display.update() # flip?

if __name__ == '__main__':
    run_game()
