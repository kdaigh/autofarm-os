import serial
import string
import time
import csv
from datetime import datetime

# @class SerialPort
# Represents a serial port of the Raspberry Pi
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
        for i in range(len(data)):
            output += data[i]
            if i < (len(data) - 1):
                output += ", "

        return output

    # Parses input by stripping non-essential characters
    def parseFromArduino(self, rawInput):
        # Decode input from Arduino
        decodedInput = rawInput.decode('utf-8').strip('\r\n')
        self.log("Input: " + decodedInput)

        # Divide data; Remove leading and trailing characters
        data = decodedInput.split(',')
        data[0] = data[0].strip('<')
        data[len(data) - 1] = data[len(data) - 1].strip('>')
        
        return data
    
    def closePort(self):
        self.serial.close()
        self.log("Serial port " + self.port + " closed")

    # Prints given message if debug is enabled
    def log(self, msg):
        if self.DEBUG == True:
            print(msg)

def getTimestamp():
    timestamp = "datetime = "
    timestamp += str(datetime.now())
    return timestamp

# @class Logger
# Logs sensor data to CSV
class Logger:
    DEBUG = True

    # Collects data into a dictionary
    # @returns Dictionary of labels and values
    def collectData(self):
        values = {}

        # Get time stamp
        values['datetime'] = str(datetime.now())

        # Get sensor data
        # NOTE: The use of [ARD1, ARD2, ...] requires use of the 10-usb-serial.rules configuration file
        self.ports = ['/dev/ttyARD1', '/dev/ttyARD2', '/dev/ttyARD3', '/dev/ttyARD4']
        for port in self.ports:
            ser = SerialPort(port, 9600)
            data = ser.readFromArduino()
            data = data.split(',')
            for datum in data:
                pair = datum.split('=')
                label = pair[0].strip(' ')
                value = pair[1].strip(' ')
                values[label] = value
            ser.closePort()
            
        return values

    # Outputs data in a CSV-style string
    def printData(self, values):
        print("\nLine added to file: ")
        counter = 1
        for label, value in values.items():
            print(value, end='')
            if counter != len(values):
                print(', ', end='')
            else:
                print()
            counter = counter + 1

    # Prints given message if debug is enabled
    def log(self, msg):
        if self.DEBUG == True:
            print(msg)

if __name__ == '__main__':
    logger = Logger()
    values = logger.collectData()
    logger.printData(values)

