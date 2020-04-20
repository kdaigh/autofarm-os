#include <stdlib.h>
#include <time.h>
#define MAXPAR 4000
#define serialPi Serial

void setup() {
    serialPi.begin(9600);  // Arduino to serial monitor
    srand((unsigned int)time(NULL));
}

void loop() {
    // Generate random sample data value
    float sample = ((float)rand()/(float)(RAND_MAX)) * MAXPAR;

    // Send  data to Raspberry Pi
    serialPi.print("<par = ");
    serialPi.print(sample, DEC);
    serialPi.println("μmol/m²s>");  

    // Wait for 5 seconds
    delay(5000);
}
