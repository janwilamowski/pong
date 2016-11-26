import pygame
from pygame import Rect
from constants import WHITE

class Player():

    def __init__(self, screen, x, y):
        self.screen = screen
        self.rect = Rect(x, y, 20, 80)

    def move_up(self, step = 2):
        if self.rect[1] > 0:
            self.rect.move_ip(0, -2)

    def move_down(self, step = 2):
        if self.rect[1] < 400:
            self.rect.move_ip(0, 2)

    def display(self):
        pygame.draw.rect(self.screen, WHITE, self.rect)

    def check_contact(self, ball):
        if self.overlaps(ball):
            ball.bounce_x()

    def overlaps(self, other):
        return self.rect.colliderect(other.rect)
