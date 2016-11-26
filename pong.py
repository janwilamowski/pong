#!/usr/bin/python

import sys
import pygame
from pygame.locals import *
from constants import BLACK
from Player import Player
from Ball import Ball

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('PONG')
    pygame.key.set_repeat(10, 10)
    clock = pygame.time.Clock()
    left_player = Player(screen, 40, 200)
    right_player = Player(screen, 580, 200)
    ball = Ball(screen, 60, 230)
    started = False

    # main loop
    while True:
        clock.tick(50) # limit to 50fps

        # game end
        if started and not screen.get_rect().colliderect(ball.rect):
            ball = Ball(screen, 60, 230)
            left_player = Player(screen, 40, 200)
            right_player = Player(screen, 580, 200)
            started = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_SPACE:
                    started = True
                    ball.moving = True
                elif event.key == K_UP and started:
                    right_player.move_up()
                elif event.key == K_DOWN and started:
                    right_player.move_down()
                # TODO: simultaneous input
                elif event.key == K_q and started:
                    left_player.move_up()
                elif event.key == K_a and started:
                    left_player.move_down()

        ball.step()
        left_player.check_contact(ball)
        right_player.check_contact(ball)

        screen.fill(BLACK)
        right_player.display()
        left_player.display()
        ball.display()

        pygame.display.update() # flip?

if __name__ == '__main__':
    run_game()
