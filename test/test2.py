# Ecrit ton programme ici ;-)

from microbit import *
import radio

radio.on()

while True:
    msg = radio.receive()
    if msg:
        display.scroll(msg)