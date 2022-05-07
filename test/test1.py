# Ecrit ton programme ici ;-)

from microbit import *
import radio

radio.on()

while True:
    if button_a.was_pressed():
        display.scroll("O")
        radio.send("O")
    else:
        display.scroll("_")
        radio.send("X")
    sleep(100)