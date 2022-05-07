# Pong System
from microbit import *
import random

ball = (3, 2)
direction = (1, 1)
plateX = 1
vit = 1

random.randint(0, 5)

while True:
    if ball[0] == 0:
        direction = (1, direction[1])
    elif ball[0] == 4:
        direction = (-1, direction[1])

    if ball[1] == 0:
        direction = (direction[0], 1)
    elif ball[1] == 3:
        direction = (direction[0], -1)

    if button_b.was_pressed() and plateX < 3:
        plateX += 1
    elif button_a.was_pressed() and plateX > 0:
        plateX -= 1

    ball = (ball[0] + direction[0], ball[1] + direction[1])
    display.clear()
    display.set_pixel(ball[0], ball[1], 9)
    display.set_pixel(plateX, 4, 9)
    display.set_pixel(plateX + 1, 4, 9)
    sleep(300 / vit)