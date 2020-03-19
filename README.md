# Autofarm OS
Our master/slave project design will involve connecting six Arduino Unos to a Raspberry Pi 4 via serial port.

## Getting Started
### Setup and Installation
First, you'll need to install setuptools for python, using the command

    python -m pip install --upgrade pip setuptools wheel

Additionally, you'll need to install the PySerial library with the commands

    sudo apt-get install python-serial

    sudo pip install pyserial

### Usage
In order to run the pilot program, first load the appropriate INO file to the Arduino Uno for each attached sensor. Then run the command

    python3 sensors.py

from inside the sensors directory.

## Examples
### Blinky Example
Upload the blinky.ino sketch to the Arduino using the Arduino IDE. Then, run the python program using
    
    python3 blinky.py

### Other Examples
The examples provided in the `examples/ArduinoPC` and `examples/ArduinoPC2` folders were provided by user Robin2 on [this thread](https://forum.arduino.cc/index.php?topic=225329.msg1810764#msg1810764).

## Built With
### Software
* [Python](https://www.python.org/) - Programming language
* [PySerial](https://pyserial.readthedocs.io/en/latest/index.html) - Module for serial port access
* [Arduino IDE](https://www.arduino.cc/en/main/software) - Microcontroller development

### Hardware
* [Raspberry Pi 4 Model B](https://www.raspberrypi.org/documentation/), *Raspberry Pi* - Computer
* [Arduino Uno](https://www.arduino.cc/en/Guide/ArduinoUno), *Arduino* - Microcontroller
* [Non-Contact Liquid Level Sensor](https://wiki.dfrobot.com/Non-contact_Liquid_Level_Sensor_XKC-Y25-T12V_SKU__SEN0204), *DFRobot* - Sensor
* [SHT20 Temperature & Humidity Sensor](https://wiki.dfrobot.com/SHT20_I2C_Temperature_%26_Humidity_Sensor__Waterproof_Probe__SKU__SEN0227), *Sensirion* - Sensor
* [Analog pH Sensor](https://wiki.dfrobot.com/PH_meter_SKU__SEN0161_), *DFRobot* - Sensor
* [Electric Solenoid Valve](https://www.amazon.com/gp/product/B010LT2OCG/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1), *BACOENG* - Actuator
* [3-Way Motorized Ball Valve](https://www.amazon.com/gp/product/B01MD2LW4I/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&th=1), *HSH-Flo* - Actuator
* [Booster Pump](https://www.amazon.com/gp/product/B003ZJMSEY/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1), *Aquatech* - Actuator
* [Aquatech Pressure Switch](https://www.amazon.com/gp/product/B07PDZQ97K/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&psc=1), *AFWFilters* - Actuator
* [SolarSystem 275](https://californialightworks.com/products/solarsystem-275), *California Lightworks* - Actuator
* [SolarSystem Controller](https://californialightworks.com/products/solarsystem-controller), *California Lightworks* - Actuator Controller

## Authors

* **Matt Cherry**, [MattCKU](https://github.com/MattCKU) - *Sensor Design, Sensor Setup*
* **Kyle Curry**, [k19c90](https://github.com/k19c90) - *Actuator Setup*
* **Kristi Daigh**, [kdaigh](https://github.com/kdaigh) - *Sensor Pilot Program*
* **Zach Freund**
* **Ethan Lefert**, [elefert400](https://github.com/elefert400)


