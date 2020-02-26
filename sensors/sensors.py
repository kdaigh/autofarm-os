import serial
import RPi.GPIO as GPIO
import time

liquid_level_pin = 5

# Open serial port
liquid_level_port = '/dev/ttyACM0'
ph_port = '/dev/ttyACM1'
baudRate = 9600
liquid_level_ser = serial.Serial(liquid_level_port, baudRate)
print("Liquid_level: Serial port " + liquid_level_port + " opened  Baudrate " + str(baudRate))
ph_ser = serial.Serial(ph_port, baudRate)
print("PH: Serial port " + ph_port + " opened  Baudrate " + str(baudRate))

# Wait for Arduino
time.sleep(1)

# Read input from liquid level sensor via Arduino
liquid_level_read = liquid_level_ser.readline()
print(liquid_level_read)

# Read input from ph sensor via Arduino


# Close serial port
liquid_level_ser.close()