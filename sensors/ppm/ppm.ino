/*
# This code is adapted from example:
 # Date   : 2019.06.00
 # Ver    : Arduino 1.8.9 IDE
 # Product: PPM Probe
 # This code will output data to the Arduino serial monitor.
 # Type commands into the Arduino serial monitor to control the EC circuit.
*/

#include <SoftwareSerial.h> 
#define serialPi Serial
#define rx 2                                          // Define what pin rx is going to be
#define tx 3                                          // Define what pin tx is going to be

SoftwareSerial myserial(rx, tx);                      // Define how the soft serial port is going to work

String sensorstring = "";                             // A string to hold the data from the Atlas Scientific product
boolean sensor_string_complete = false;               // Have we received all the data from the Atlas Scientific product

void setup() {                                              // Set up the hardware
    serialPi.begin(9600);                                   // Set baud rate for the hardware serial port_0 to 9600
    myserial.begin(9600);                                   // Set baud rate for the software serial port to 9600      
    sensorstring.reserve(30);                               // Set aside some bytes for receiving data from Atlas Scientific product
}

void loop() {
    if (myserial.available() > 0) {                         // if we see that the Atlas Scientific product has sent a character
        char inchar = (char)myserial.read();                // get the char we just received
        sensorstring += inchar;                             // add the char to the var called sensorstring
        if (inchar == '\r') {                               // if the incoming character is a <CR>
            sensor_string_complete = true;                  // set the flag
        }
    }

    if (sensor_string_complete == true) {                   // if a string from the Atlas Scientific product has been received in its entirety
        if (isdigit(sensorstring[0]) == false) {            // if the first character in the string is a digit
            serialPi.println(sensorstring);                 // send that string to the PC's serial monitor
        } else {                                            // if the first character in the string is NOT a digit
            print_EC_data();                                // then call this function 
        }
        sensorstring = "";                                  // clear the string
        sensor_string_complete = false;                     // reset the flag used to tell if we have received a completed string from the Atlas Scientific product
        
        // Wait for 3 seconds
        delay(3000);
    }
}

// Parses the string
void print_EC_data(void) {                            
    char sensorstring_array[30];
    char *EC;                       // EC
    char *TDS;                      // TDS
    char *SAL;                      // Salinity
    char *GRAV;                     // Specific gravity
    float f_ec;    
    
    sensorstring.toCharArray(sensorstring_array, 30);
    EC = strtok(sensorstring_array, ",");
    TDS = strtok(NULL, ",");
    SAL = strtok(NULL, ",");
    GRAV = strtok(NULL, ",");
    f_ec = atof(EC); 

    // Send  data to Raspberry Pi
    String outputstring = "";
    outputstring += "<EC = ";
    outputstring += EC;
    outputstring += ", TDS = ";
    outputstring += TDS;
    outputstring += ", SAL = ";
    outputstring += SAL;
    outputstring += ">";
    serialPi.println(outputstring);

    // serialPi.print("<EC = ");
    // serialPi.print(f_ec, 2);
    // serialPi.print(", TDS = ");
    // serialPi.print(TDS);
    // serialPi.print(", SAL = ");
    // serialPi.print(SAL);
    // serialPi.println(">");
}































