import pygame
from constants import white

class Ball():

    def __init__(self, screen, pos_x, pos_y):
        self.screen = screen
        self.pos = (pos_x, pos_y)
        self.moving = False
        self.direction = None

    def step(self):
        if not self.moving: return

    def display(self):
        pygame.draw.rect(self.screen, white, (self.pos[0], self.pos[1], 20, 20))
