# Pong System
from microbit import *

class Pong:

    def __init__(self):
        self.ball = (3, 2)
        self.direction = (1, 1)
        self.plateX = 1
        self.vit = 1

    def display_pong(self):
        display.clear()
        display.set_pixel(self.ball[0], self.ball[1], 9)
        display.set_pixel(self.plateX, 4, 9)
        display.set_pixel(self.plateX + 1, 4, 9)

    def update_plate(self):
        if button_b.was_pressed() and self.plateX < 3:
            self.plateX += 1
        elif button_a.was_pressed() and self.plateX > 0:
            self.plateX -= 1

    def update_ball(self):
        if self.ball[0] == 0:
            self.direction = (1, self.direction[1])
        elif self.ball[0] == 4:
            self.direction = (-1, self.direction[1])

        if self.ball[1] == 0:
            self.direction = (self.direction[0], 1)
        elif self.ball[1] == 3:
            self.direction = (self.direction[0], -1)

        self.ball = (
            self.ball[0] + self.direction[0],
            self.ball[1] + self.direction[1]
        )

game = Pong()

while True:
    game.update_ball()
    game.update_plate()
    game.display_pong()
    sleep(300 / game.vit)