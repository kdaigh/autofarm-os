import serial
import RPi.GPIO as GPIO
import time

liquid_level_pin = 5

# Open serial port
serPort = '/dev/ttyACM0'
baudRate = 9600
ser = serial.Serial(serPort, baudRate)
print("Serial port " + serPort + " opened  Baudrate " + str(baudRate))

# Wait for Arduino
time.sleep(1)

# Read input from liquid level sensor via Arduino
read_ser = ser.readline()
print(read_ser)

# Close serial port
ser.close()