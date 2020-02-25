# Autofarm OS
Our master/slave project design will involve connecting five Arduino Unos to a Raspberry Pi 4 via serial port.

## Getting Started
First, you'll need to install setuptools for python, using the command

    python -m pip install --upgrade pip setuptools wheel

Additionally, you'll need to install the PySerial library with the command

    pip install pyserial

## Blinky Example
Upload the blinky.ino sketch to the Arduino using the Arduino IDE. Then, run the python program using
    
    python3 blinky.py