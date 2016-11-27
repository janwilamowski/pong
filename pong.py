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
        self.use_ai = 'ai' in args
        no_sound = 'nosound' in args
        self.setup_sounds(no_sound)
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

    def setup_sounds(self, no_sound):
        if no_sound:
            self.sounds = {}
            return

        self.sounds = {
            'blip': pygame.mixer.Sound('sfx/blip5.wav'),
            'blop': pygame.mixer.Sound('sfx/blip4.wav'),
            'gameover': pygame.mixer.Sound('sfx/gameover.wav')
        }

    def play(self, sound):
        if sound in self.sounds:
            self.sounds[sound].play()

    def run(self):
        # globals
        pygame.display.set_caption('PONG')
        pygame.key.set_repeat(10, 10)
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 36)

        left_score = right_score = 0
        left_score_pos = pygame.Rect(260, 230, 50, 30)
        right_score_pos = pygame.Rect(410, 230, 50, 30)


        # main loop
        while True:
            clock.tick(50) # limit to 50fps

            # game end
            if self.started and self.ball.is_offscreen():
                self.play('gameover')
                if self.ball.rect.x < 0:
                    right_score += 1
                else:
                    left_score += 1
                self.init()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYUP and event.key == K_SPACE:
                    if not self.started:
                        self.play('blop')
                    self.started = not self.started
                    self.ball.moving = not self.ball.moving

            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                pygame.quit()
                sys.exit()
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
                    self.play('blip')
                if self.left_player.check_contact(self.ball) \
                        or self.right_player.check_contact(self.ball):
                    self.bounces += 1
                    self.play('blop')
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
