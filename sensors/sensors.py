import serial
import time

liquid_level_pin = 5

# Open serial port
liquid_level_port = '/dev/ttyACM0'
ph_port = '/dev/ttyACM1'
hygrometer_port = '/dev/ttyACM2'
baudRate = 9600
liquid_level_ser = serial.Serial(liquid_level_port, baudRate)
print("Liquid_level: Serial port " + liquid_level_port + " opened  Baudrate " + str(baudRate))
ph_ser = serial.Serial(ph_port, baudRate)
print("PH: Serial port " + ph_port + " opened  Baudrate " + str(baudRate))
hygrometer_ser = serial.Serial(hygrometer_port, baudRate)
print("Hygrometer: Serial port " + hygrometer_port + " opened  Baudrate " + str(baudRate))

# Wait for Arduino
time.sleep(1)

# Read input from liquid level sensor via Arduino
liquid_level_read = liquid_level_ser.readline()
print(liquid_level_read)
time.sleep(1)

# Read input from ph sensor via Arduino
ph_read = ph_ser.readline()
print(ph_read)
time.sleep(1)

# Read input from Hygrometer via Arduino
hygrometer_read = hygrometer_ser.readline()
print(hygrometer_read)
time.sleep(1)

# Close serial port
liquid_level_ser.close()
ph_ser.close()
hygrometer_ser.close()