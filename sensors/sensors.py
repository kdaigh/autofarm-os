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
        # TODO: Add way of checking which ports are open and then reading from
        # open ports only (via iteration)
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
        self.log("Data: " + str(data))
        
        return data
    
    def closePort(self):
        self.serial.close()

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

    # Collects data into values array
    # @returns Values array
    def collectData(self):
        values = []

        # Get time stamp
        values.append("datetime = " + str(datetime.now()))
        self.log('timestamp: ' + str(datetime.now()))

        # Get sensor data
        self.ports = ['/dev/ttyARD1', '/dev/ttyARD2', '/dev/ttyARD3', '/dev/ttyARD4']
        for port in self.ports:
            ser = SerialPort(port, 9600)
            values.append(ser.readFromArduino())
            ser.closePort()
            self.log("Values: " + str(values))
            
        return values

    def printData(self):
        # Print data into CSV files
        for value in self.values:
            pass
            # TODO

            # PREV CODE: Used dictionary to print a line of data from a 
            # sensor to an EXISTING file named according to port (i.e. 'port1.csv')
            # with open('data/' + file + '.csv', 'a+', newline='') as f:
            #     writer = csv.writer(f)
            #     writer.writerow(data)
    
    # Prints given message if debug is enabled
    def log(self, msg):
        if self.DEBUG == True:
            print(msg)

if __name__ == '__main__':
    logger = Logger()
    logger.collectData()
    logger.printData()

