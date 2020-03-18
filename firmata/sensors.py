#!/usr/bin/env python3.4

import pyfirmata as firmata
import time
board = firmata.Arduino('/dev/ttyACM0')
pin13 = board.get_pin('d:5:i') 
while True:
    time.sleep(1)
    liquid_level = pin13.read()
    time.sleep(1)
    print("liquid_level = " + str(liquid_level))
    pin13.write(0)