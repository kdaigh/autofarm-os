#!/usr/bin/env python3.4

import pyfirmata as firmata
import time
board = firmata.Arduino('/dev/ttyACM0')
pin5 = board.get_pin('d:5:p') 
while True:
    time.sleep(1)
    liquid_level = pin5.read()
    time.sleep(1)
    print("liquid_level = " + str(liquid_level))