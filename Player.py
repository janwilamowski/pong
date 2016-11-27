import pygame
from pygame import Rect
from constants import WHITE

class Player():

    def __init__(self, screen, x, y):
        self.screen = screen
        self.rect = Rect(x, y, 20, 80)

    def move_up(self):
        if self.rect.y > 0:
            self.rect.move_ip(0, -4)

    def move_down(self):
        if self.rect.y < 400:
            self.rect.move_ip(0, 4)

    def display(self):
        pygame.draw.rect(self.screen, WHITE, self.rect)

    def check_contact(self, ball):
        """
        Checks whether this player has contact with the given ball. If so, will bounce the ball
        in the appropriate direction.

        Uses PyGame's overlap functionality which is convenient but somewhat imprecise.

        @return bool whether there's a contact between player and ball
        """
        if not self.overlaps(ball):
            return False

        if ball.moving_right:
            x_diff = abs(ball.rect.right - self.rect.left)
        else:
            x_diff = abs(ball.rect.left - self.rect.right)

        if ball.moving_up:
            y_diff = abs(ball.rect.top - self.rect.bottom)
        else:
            y_diff = abs(ball.rect.bottom - self.rect.top)

        if x_diff < y_diff and ball.rect.x:
            ball.bounce_x()
        elif x_diff > y_diff:
            ball.bounce_y()
        else:
            # corner bounce
            ball.bounce_x()
            ball.bounce_y()

        return True

    def overlaps(self, other):
        return self.rect.colliderect(other.rect)

    def ai_move(self, ball):
        if not ball.moving: return

        if ball.moving_right:
            # go back to center
            target_y = 200
        else:
            # follow ball
            target_y = ball.rect.y - 30

        if self.rect.y < target_y:
            self.move_down()
        elif self.rect.y > target_y:
            self.move_up()
