import pygame
from pygame import Rect
from constants import WHITE
import math

class Ball():

    def __init__(self, screen, x, y, speed = 4, angle = 45):
        self.screen = screen
        self.rect = Rect(x, y, 20, 20)
        self.moving = False
        self.moving_right = True
        self.moving_up = angle > 0
        self.speed = speed
        self.angle = math.pi * abs(angle)/180

    def step(self):
        if not self.moving: return

        dx = int(round(math.cos(self.angle) * self.speed))
        dy = int(round(math.sin(self.angle) * self.speed))

        if not self.moving_right:
            dx *= -1
        if self.moving_up:
            dy *= -1

        self.rect.move_ip(dx, dy)

        if self.rect.y < 0 or self.rect.y > 460:
            self.bounce_y()
            return True

        return False

    def bounce_x(self):
            self.moving_right = not self.moving_right

    def bounce_y(self):
            self.moving_up = not self.moving_up

    def display(self):
        pygame.draw.rect(self.screen, WHITE, self.rect)
