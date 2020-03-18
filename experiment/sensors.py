import serial
import string
import time

class SerialPort:
    DEBUG = True

    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.serial = serial.Serial(port, self.baudrate)
        self.log("Serial port " + self.port + " opened  Baudrate " + str(self.baudrate))


    def readFromSensors(self):
        while True:
            if self.serial.in_waiting > 0:
                rawInput = self.serial.readline()
                decodedInput = rawInput.decode('utf-8').strip('\r\n')

                liquid_level = self.parseLiquidLevel(decodedInput)
                print(liquid_level)
    
    # Parses input by stripping non-essential characters
    def parseLiquidLevel(self, decodedInput):
        parsedInput = decodedInput.strip('<')
        parsedInput = decodedInput.strip('>')
        return parsedInput

    # Prints given message if debug is enabled
    def log(self, msg):
        if self.DEBUG == True:
            print(msg)

if __name__ == '__main__':
    arduino = SerialPort('/dev/ttyACM0', 9600)
    arduino.readFromSensors()