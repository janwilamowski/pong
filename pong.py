#!/usr/bin/python

import sys
import pygame
from pygame.locals import *
from Player import Player
from Ball import Ball

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('PONG')
    pygame.key.set_repeat(10, 10)
    clock = pygame.time.Clock()
    black = (0, 0, 0)
    left_player = Player(screen, 40, 200)
    right_player = Player(screen, 580, 200)
    ball = Ball(screen, 200, 200)

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
                elif event.key == K_UP:
                    right_player.move_up()
                elif event.key == K_DOWN:
                    right_player.move_down()
                elif event.key == K_q:
                    left_player.move_up()
                elif event.key == K_a:
                    left_player.move_down()

        screen.fill(black)
        right_player.display()
        left_player.display()
        ball.display()

        pygame.display.update() # flip?

if __name__ == '__main__':
    run_game()
