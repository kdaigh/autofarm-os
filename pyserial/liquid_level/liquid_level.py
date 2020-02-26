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
GPIO.input(liquid_level_pin)
time.sleep(1)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(liquid_level_pin, GPIO.IN)
# read_ser = ser.readline()
# print(read_ser)

# Close serial port
ser.close()