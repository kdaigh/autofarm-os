import serial
import time

# Open serial port
serPort = '/dev/ttyACM0'
baudRate = 9600
ser = serial.Serial(serPort, baudRate)
print("Serial port " + serPort + " opened  Baudrate " + str(baudRate))

# Wait for Arduino
time.sleep(5)

# Read input from Arduino
read_ser = ser.readline()
print(read_ser)

# Close serial port
ser.close()