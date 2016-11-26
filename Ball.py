import pygame
from constants import WHITE

class Ball():

    def __init__(self, screen, pos_x, pos_y):
        self.screen = screen
        self.pos = (pos_x, pos_y)
        self.moving = False
        self.moving_right = True
        self.moving_up = True

    def step(self):
        if not self.moving: return

        if self.moving_right:
            if self.moving_up:
                self.pos = (self.pos[0] + 4, self.pos[1] - 4)
            else:
                self.pos = (self.pos[0] + 4, self.pos[1] + 4)
        else:
            if self.moving_up:
                self.pos = (self.pos[0] - 4, self.pos[1] - 4)
            else:
                self.pos = (self.pos[0] - 4, self.pos[1] + 4)

    def display(self):
        pygame.draw.rect(self.screen, WHITE, (self.pos[0], self.pos[1], 20, 20))
