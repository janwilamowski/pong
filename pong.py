#!/usr/bin/python

import sys
import pygame
from pygame.locals import *
from constants import BLACK, WHITE
from Player import Player
from Ball import Ball
import random

class Game():
    def __init__(self, args):
        random.seed()
        pygame.init()
        self.use_ai = len(args) > 0 and args[0] == 'ai'
        self.init()

    def init(self):
        # game state
        self.started = False
        self.screen = pygame.display.set_mode((640, 480))
        self.left_player = Player(self.screen, 40, 200)
        self.right_player = Player(self.screen, 580, 200)
        self.speed = 6
        self.bounces = 0
        angle = random.randint(30, 60)
        angle *= random.choice([-1, 1])
        self.ball = Ball(self.screen, 60, 230, self.speed, angle)

    def run(self):
        # globals
        pygame.display.set_caption('PONG')
        pygame.key.set_repeat(10, 10)
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 36)

        left_score = right_score = 0
        left_score_pos = pygame.Rect(260, 230, 50, 30)
        right_score_pos = pygame.Rect(410, 230, 50, 30)

        blip = pygame.mixer.Sound('sfx/blip5.wav')
        blop = pygame.mixer.Sound('sfx/blip4.wav')
        gameover = pygame.mixer.Sound('sfx/gameover.wav')

        # main loop
        while True:
            clock.tick(50) # limit to 50fps

            # game end
            if self.started and not self.screen.get_rect().colliderect(self.ball.rect):
                gameover.play()
                if self.ball.rect.x < 0:
                    right_score += 1
                else:
                    left_score += 1
                self.init()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                pygame.quit()
                sys.exit()
            if keys[K_SPACE] and not self.started:
                self.started = True
                self.ball.moving = True
                blop.play()
            if keys[K_UP] and self.started:
                self.right_player.move_up()
            if keys[K_DOWN] and self.started:
                self.right_player.move_down()
            if keys[K_q] and self.started and not self.use_ai:
                self.left_player.move_up()
            if keys[K_a] and self.started and not self.use_ai:
                self.left_player.move_down()

            self.screen.fill(BLACK)

            if self.started:
                if self.ball.step():
                    blip.play()
                if self.left_player.check_contact(self.ball) or self.right_player.check_contact(self.ball):
                    self.bounces += 1
                    blop.play()
                # increase speed
                if self.bounces > 5:
                    self.speed += 1
                    self.ball.speed = self.speed
                    self.bounces = 0
                if self.use_ai:
                    self.left_player.ai_move(self.ball)
            else:
                # show score
                left_score_text = font.render(str(left_score), 1, WHITE)
                self.screen.blit(left_score_text, left_score_pos)
                right_score_text = font.render(str(right_score), 1, WHITE)
                self.screen.blit(right_score_text, right_score_pos)

            self.right_player.display()
            self.left_player.display()
            self.ball.display()

            pygame.display.flip()

if __name__ == '__main__':
    game = Game(sys.argv[1:])
    game.run()
