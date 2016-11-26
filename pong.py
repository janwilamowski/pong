#!/usr/bin/python

import sys
import pygame
from pygame.locals import *
from constants import BLACK, WHITE
from Player import Player
from Ball import Ball

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('PONG')
    pygame.key.set_repeat(10, 10)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    left_player = Player(screen, 40, 200)
    right_player = Player(screen, 580, 200)
    ball = Ball(screen, 60, 230)
    left_score = right_score = 0
    left_score_pos = pygame.Rect(260, 230, 50, 30)
    right_score_pos = pygame.Rect(410, 230, 50, 30)
    started = False

    # main loop
    while True:
        clock.tick(50) # limit to 50fps

        # game end
        if started and not screen.get_rect().colliderect(ball.rect):
            if ball.rect.x < 0:
                right_score += 1
            else:
                left_score += 1

            ball = Ball(screen, 60, 230)
            left_player = Player(screen, 40, 200)
            right_player = Player(screen, 580, 200)
            started = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[K_SPACE] and not started:
            started = True
            ball.moving = True
        if keys[K_UP] and started:
            right_player.move_up()
        if keys[K_DOWN] and started:
            right_player.move_down()
        if keys[K_q] and started:
            left_player.move_up()
        if keys[K_a] and started:
            left_player.move_down()

        screen.fill(BLACK)

        if started:
            ball.step()
            left_player.check_contact(ball)
            right_player.check_contact(ball)
        else:
            # show score
            left_score_text = font.render(str(left_score), 1, WHITE)
            screen.blit(left_score_text, left_score_pos)
            right_score_text = font.render(str(right_score), 1, WHITE)
            screen.blit(right_score_text, right_score_pos)

        right_player.display()
        left_player.display()
        ball.display()

        pygame.display.update() # flip?

if __name__ == '__main__':
    run_game()
