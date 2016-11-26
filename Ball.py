import pygame
from pygame import Rect
from constants import WHITE

class Ball():

    def __init__(self, screen, x, y):
        self.screen = screen
        self.rect = Rect(x, y, 20, 20)
        self.moving = False
        self.moving_right = True
        self.moving_up = True

    def step(self):
        if not self.moving: return

        if self.moving_right:
            if self.moving_up:
                self.rect.move_ip(4, -4)
            else:
                self.rect.move_ip(4, 4)
        else:
            if self.moving_up:
                self.rect.move_ip(-4, -4)
            else:
                self.rect.move_ip(-4, 4)

        if self.rect.y < 0 or self.rect.y > 460:
            self.bounce_y()

    def bounce_x(self):
            self.moving_right = not self.moving_right

    def bounce_y(self):
            self.moving_up = not self.moving_up

    def display(self):
        pygame.draw.rect(self.screen, WHITE, self.rect)
