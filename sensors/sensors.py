import serial
import string
import time
import csv
from datetime import datetime
from random import seed
from random import random
from random import randint

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

        # Add dummy value for par sensor
        values['par'] = self.generateDummyValue(1200, 1275)
            
        return values

    # Outputs data in a CSV-style string
    def printData(self, values, header):
        self.log("\nLine added to file: ")
        counter = 1
        labelString = ""
        dataString = ""
        for label, value in values.items():
            labelString += label
            dataString += str(value)
            if counter != len(values):
                labelString += ", "
                dataString += ", "
            else:
                labelString += "\n"
                dataString += "\n"
            counter = counter + 1

        if header == True:
            with open('data/data.csv', 'w') as file:
                file.write(labelString)
                self.log(labelString)
        else:
            with open('data/data.csv', 'a') as file:
                file.write(dataString)
                self.log(dataString)

    def generateDummyValue(self, min, max):
        # Generate random float between 0 and 1
        seed(1)
        floatNum = random()

        # Generate random integer in provided range
        intNum = randint(min, max)

        return floatNum + intNum


    # Prints given message if debug is enabled
    def log(self, msg):
        if self.DEBUG == True:
            print(msg)

if __name__ == '__main__':
    logger = Logger()
    header = True
    for _ in range(0, 3):
        values = logger.collectData()
        logger.printData(values, header)
        label = False

