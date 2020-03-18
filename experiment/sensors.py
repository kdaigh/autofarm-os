import serial
import string
import time
import datetime

class SerialPort:
    DEBUG = True

    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.serial = serial.Serial(port, self.baudrate)
        self.log("Serial port " + self.port + " opened  Baudrate " + str(self.baudrate))

    def readFromArduino(self):
        # Wait for Arduino
        while self.serial.in_waiting <= 0:
            pass

        # Read sensor data
        rawInput = self.serial.readline()
        data = self.parseFromArduino(rawInput)
        output = ""
        for datum in data:
            output += datum
            output += ", "
        return output

    # Parses input by stripping non-essential characters
    def parseFromArduino(self, rawInput):
        # Decode input from Arduino
        decodedInput = rawInput.decode('utf-8').strip('\r\n')

        # Divide data; Remove leading and trailing characters
        data = decodedInput.split(',')
        data[0] = data[0].strip('<')
        data[len(data) - 1] = data[len(data) - 1].strip('>')
        self.log("Data: " + str(data))
        
        return data
    
    def closePort(self):
        self.serial.close()

    # Prints given message if debug is enabled
    def log(self, msg):
        if self.DEBUG == True:
            print(msg)

def getTimestamp():
    timestamp = str(datetime.datetime.now())
    return timestamp

if __name__ == '__main__':
    output = getTimestamp()
    output += ", "

    liquidLevelPort = SerialPort('/dev/ttyACM0', 9600)
    output += liquidLevelPort.readFromArduino()
    liquidLevelPort.closePort()

    phPort = SerialPort('/dev/ttyACM1', 9600)
    output += phPort.readFromArduino()
    phPort.closePort()

