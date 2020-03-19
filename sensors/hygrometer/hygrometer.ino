/*!
 * Adapted from the following example
 * @file  DFRobot_SHT20_test.ino
 * @brief DFRobot's SHT20 Humidity And Temperature Sensor Module
 * @n     This example demonstrates how to read the user registers to display resolution and other settings.
 *        Uses the SHT20 library to display the current humidity and temperature.
 *        Open serial monitor at 9600 baud to see readings.
 *        Errors 998 if not sensor is detected. Error 999 if CRC is bad.
 * Hardware Connections:
 * -VCC = 3.3V
 * -GND = GND
 * -SDA = A4 (use inline 330 ohm resistor if your board is 5V)
 * -SCL = A5 (use inline 330 ohm resistor if your board is 5V)
 */

#include <Wire.h>
#include "DFRobot_SHT20.h"
#define serialPi Serial

DFRobot_SHT20    sht20;

void setup()
{
    serialPi.begin(9600);  // Arduino to serial monitor

    // Init SHT20 Sensor
    sht20.initSHT20();                                 

    // Check SHT20 Sensor
    delay(100);
    sht20.checkSHT20();                                 
}

void loop()
{
    // Read data from sensor
    float temp = sht20.readTemperature();               // Read Temperature
    float humdity = sht20.readHumidity();               // Read Humidity

    // Send  data to Raspberry Pi
    serialPi.print("<temperature = ");
    serialPi.print(temp, 1);
    serialPi.print("°C, humidity= ");
    serialPi.print(humdity, 2);
    serialPi.println("%>");

    // Wait for 5 seconds
    delay(5000);
}