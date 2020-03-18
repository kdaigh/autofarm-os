# AutofarmOS

Firmata is a protocol for communicating with microcontrollers from software on a host computer. The protocol can be implemented in firmware on any microcontroller architecture as well as software on any host computer software package.

This project is built using the PyFirmata library.

## Getting Started

### Setup and Installation

*1.* Load the [StandardFirmata.ino](https://github.com/firmata/arduino/blob/master/examples/StandardFirmata/StandardFirmata.ino) sketch to the Arduino.

*2.* Install Firmata on the Pi with the following commands
    
    sudo apt-get install python-serial mercurial 
    python3 -m pip install pyfirmata` 

You can ensure that this was completed successfully, open Python Idle and run 
    
    import pyfirmata


### Blinky Test
Test the setup and installation by running

    python blinky.py

### Versioning

* pip - 20.0.2
* Python - 3.4.4
