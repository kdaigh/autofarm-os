import serial
import time

# Open serial port
serPort = '/dev/ttyACM0'
baudRate = 9600
ser = serial.Serial(serPort, baudRate)
print("Serial port " + serPort + " opened  Baudrate " + str(baudRate))

# Wait for Arduino
time.sleep(5)

# Send encoded "3" to Arduino
num_blinks = "3"
ser.write(bytes(num.encode("ascii")))

# Close serial port
ser.close()