import unittest
from Ball import Ball

class BallTest(unittest.TestCase):

    def test_step_45_deg(self):
        self.check_step(45, 7, 7)

    def test_step_30_deg(self):
        self.check_step(30, 9, 5)

    def test_step_0_deg(self):
        self.check_step(0, 10, 0)

    def check_step(self, angle, dx, dy):
        # given
        ball = Ball(None, 0, 0, 10, angle)
        ball.moving = True
        ball.moving_up = False

        # when
        ball.step()

        # then
        self.assertEquals(dx, ball.rect.x)
        self.assertEquals(dy, ball.rect.y)
