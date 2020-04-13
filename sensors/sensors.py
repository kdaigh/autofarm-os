import serial
import string
import time

import csv
import psutil as ps
from datetime import datetime
from time import sleep

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

class Logger:
    data_dict = {}

    def collect_data(self):
        #get time stamp
        self.data_dict['cpu'] = (datetime.now(), *ps.cpu_times())
        #pull sensor data
        port = SerialPort('/dev/ttyACM0', 9600)
        self.data_dict['port1'] = (port)
        port = SerialPort('/dev/ttyACM1', 9600)
        self.data_dict['port2'] = port
        # port = SerialPort('/dev/ttyACM2', 9600)
        # self.data_dict['port3'] = port

    def print_data(self):
        #print data into CSV files
        for file, data in self.data_dict.items():
            with open('data/' + file + '.csv', 'a+', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)

if __name__ == '__main__':
    output = "<"
    output += getTimestamp()
    output += ", "

    # TODO: Add way of checking which ports are open and then reading from
    # open ports only (via iteration)

    # # Open port ACM0
    # port = SerialPort('/dev/ttyACM0', 9600)
    # output += port.readFromArduino()
    # output += ", "
    # port.closePort()

    # # Open port ACM1
    # port = SerialPort('/dev/ttyACM1', 9600)
    # output += port.readFromArduino()
    # output += ", "
    # port.closePort()

    # # Open port ACM2
    # port = SerialPort('/dev/ttyACM2', 9600)
    # output += port.readFromArduino()
    # port.closePort()

    # output += ">"

    # print(output)

    logger = Logger()
    logger.collect_data()
    logger.print_data()

