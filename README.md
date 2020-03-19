# Autofarm OS
Our master/slave project design will involve connecting six Arduino Unos to a Raspberry Pi 4 via serial port.

## Getting Started
First, you'll need to install setuptools for python, using the command

    python -m pip install --upgrade pip setuptools wheel

Additionally, you'll need to install the PySerial library with the commands

    sudo apt-get install python-serial

    sudo pip install pyserial

## Examples
### Blinky Example
Upload the blinky.ino sketch to the Arduino using the Arduino IDE. Then, run the python program using
    
    python3 blinky.py

### Other Examples
The examples provided in the `examples/ArduinoPC` and `examples/ArduinoPC2` folders were provided by user Robin2 on [this thread](https://forum.arduino.cc/index.php?topic=225329.msg1810764#msg1810764).