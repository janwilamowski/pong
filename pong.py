#!/usr/bin/python

import sys
import pygame
from pygame.locals import *
from constants import BLACK, WHITE
from Player import Player
from Ball import Ball
import random
import os
import module_locator

base_dir = module_locator.module_path()

class Game():
    def __init__(self, args):
        random.seed()
        pygame.init()
        self.use_ai = 'ai' in args
        self.no_sound = 'nosound' in args
        self.screenshot_counter = 0
        self.setup_sounds()
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

    def setup_sounds(self):
        self.sounds = {
            'blip': pygame.mixer.Sound(os.path.join(base_dir, 'sfx', 'blip5.wav')),
            'blop': pygame.mixer.Sound(os.path.join(base_dir, 'sfx', 'blip4.wav')),
            'gameover': pygame.mixer.Sound(os.path.join(base_dir, 'sfx', 'gameover.wav'))
        }

    def play(self, sound):
        if not self.no_sound and sound in self.sounds:
            self.sounds[sound].play()

    def screenshot(self):
        filename = "screenshot{c}.jpg".format(c=self.screenshot_counter)
        self.screenshot_counter += 1
        pygame.image.save(self.screen, os.path.join(base_dir, filename))

    def run(self):
        # globals
        pygame.display.set_caption('PONG')
        pygame.key.set_repeat(10, 10)
        clock = pygame.time.Clock()
        font_file = os.path.join(base_dir, 'fonts', 'DejaVuSansMono.ttf')
        small_font = pygame.font.Font(font_file, 16)
        big_font = pygame.font.Font(font_file, 36)

        left_score = right_score = 0
        left_score_pos = pygame.Rect(260, 230, 50, 30)
        right_score_pos = pygame.Rect(410, 230, 50, 30)

        help_text = []
        with open(os.path.join(base_dir, 'help.txt'), 'r') as help_file:
            for line in help_file:
                help_text.append(line[:-1])
        show_help = False

        def pause():
            if not self.started:
                self.play('blop')
            self.started = not self.started
            self.ball.moving = not self.ball.moving

        def unpause():
            pause()

        def display_score():
            left_score_text = big_font.render(str(left_score), 1, WHITE)
            self.screen.blit(left_score_text, left_score_pos)
            right_score_text = big_font.render(str(right_score), 1, WHITE)
            self.screen.blit(right_score_text, right_score_pos)

        def display_help():
            help_text_pos = pygame.Rect(200, 100, 540, 380)
            for line in help_text:
                help_line = small_font.render(line, 1, WHITE)
                self.screen.blit(help_line, help_text_pos)
                help_text_pos.move_ip(0, 20)

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
                elif event.type == KEYUP:
                    if show_help:
                        show_help = False
                        if self.started:
                            unpause()
                        continue
                    if event.key == K_SPACE:
                        pause()
                    if event.key == K_F1:
                        show_help = not show_help
                        if self.started:
                            pause()
                    if event.key == K_F3:
                        self.use_ai = not self.use_ai
                    if event.key == K_F4:
                        self.no_sound = not self.no_sound
                    if event.key == K_F5:
                        self.screenshot()

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
            elif show_help:
                display_help()
            else:
                display_score()

            self.right_player.display()
            self.left_player.display()
            if not show_help:
                self.ball.display()

            pygame.display.flip()

if __name__ == '__main__':
    game = Game(sys.argv[1:])
    game.run()
