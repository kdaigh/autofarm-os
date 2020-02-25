from nanpy import ArduinoApi
from nanpy import SerialManager
import datetime

liquid_level_sensor_pin = 5

# Open connection
connection = SerialManager(device='/dev/ttyACM0')
a = ArduinoApi(connection=connection)

# Set pins
a.pinMode(liquid_level_sensor_pin, a.INPUT)

# Read from pins
liquid_level = a.digitalRead(liquid_level_sensor_pin)

# Output sensor data
timestamp = str(datetime.datetime.now())
output += timestamp + ", liquid_level= " + str(liquid_level)