from nanpy import ArduinoApi
from nanpy import SerialManager
connection = SerialManager(device='/dev/ttyACM0')
a = ArduinoApi(connection=connection)
a.pinMode(13, a.OUTPUT)
a.digitalWrite(13, a.HIGH)