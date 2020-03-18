import serial, string, time

# Open serial port
serPort = '/dev/ttyACM0'
baudRate = 9600
ser = serial.Serial(serPort, baudRate)
print("Serial port " + serPort + " opened  Baudrate " + str(baudRate))

#The following block of code works like this:
#If serial data is present, read the line, decode the UTF8 data,
#...remove the trailing end of line characters
#...split the data into temperature and humidity
#...remove the starting and ending pointers (< >)
#...print the output
while True:
        if ser.in_waiting > 0:
            rawserial = ser.readline()
            cookedserial = rawserial.decode('utf-8').strip('\r\n')
            # datasplit = cookedserial.split(',')
            # temperature = datasplit[0].strip('<')
            # humidity = datasplit[1].strip('>')
            liquid_level = cookedserial.strip('<')
            liquid_level = liquid_level.strip('>')
            print(liquid_level)
            # print(humidity)