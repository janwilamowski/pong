import pygame

white = (255, 255, 255)

class Player():

    def __init__(self, screen, pos_x, pos_y):
        self.screen = screen
        self.pos = (pos_x, pos_y)

    def move_up(self, step = 2):
        if self.pos[1] > 0:
            self.pos = (self.pos[0], self.pos[1] - 2)

    def move_down(self, step = 2):
        if self.pos[1] < 400:
            self.pos = (self.pos[0], self.pos[1] + 2)

    def display(self):
        pygame.draw.rect(self.screen, white, (self.pos[0], self.pos[1], 20, 80))
