import serial
import time

class SerialPort:
    BAUDRATE = 9600
    TIMEOUT = 5
    DEBUG = True
    PING = "P"
    PING_REPLY = "A"
    READ = "R"
    END_CHAR = "E"

    def __init__(self, port):
        self.port = port
        self.serial = serial.Serial(port, self.BAUDRATE, self.TIMEOUT)
        self.log("Serial port " + self.port + " opened")

        if self.pingArduino() == True:
            self.log("System ready")

    # Returns true if Arduino responds to ping; False, otherwise.
    def pingArduino(self):
        self.log("Verifying system")
        self.serial.flushInput()
        sent = self.serial.write(self.PING.encode("ascii"))
        self.log("Sending ping " + str(sent))
        reply = self.serial.read(1)
        if len(reply) < 1: 
            self.log("No reply from port: " + str(self.port))
            return False
        if reply != self.PING_REPLY:
            self.log("Unexpected reply from Arduino: " + reply)
            return True
        return True
    
    def readFromArduino(self):
        msg = self.serial.readline()
        return msg.rstrip()

    def readSensor(self):
        self.log("Attempting to read data from sensor")
        self.serial.write(self.READ.encode())
        sensor_read = self.readFromArduino()
        assert(sensor_read.endswith(self.END_CHAR))
        return float(sensor_read.rstrip(self.END_CHAR))

    # Prints given message if debug is enabled
    def log(self, msg):
        if self.DEBUG == True:
            print(msg)

# Open serial port
# arduino_ports = ['/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2']
# baudRate = 9600

# Wait for Arduino
# TODO

# For each port, read input from sensor(s)
# for port in arduino_ports:
#     # Open port
#     ser = serial.Serial(port, baudRate)
#     print("Serial port " + port + " opened; Baudrate " + str(baudRate))

#     # Read data and print to terminal
#     read_ser = ser.readline()
#     print(read_ser)
#     ser.close()

if __name__ == '__main__':
    ard = SerialPort("/dev/ttyAMA0")
    ard_read = ard.readSensor()
    print(ard_read)
