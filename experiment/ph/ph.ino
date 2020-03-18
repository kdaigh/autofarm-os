/*
# This code is adapted from example by:
 # Editor : YouYou
 # Date   : 2013.10.12
 # Ver    : 0.1
 # Product: pH meter
 # SKU    : SEN0161
*/

// pH meter Analog output to Arduino Analog Input 0
#define sensorPin 0
#define serialPi Serial

unsigned long int avgValue;  // Store the average value of the sensor feedback
float b;
int buf[10],temp;

void setup() {
    serialPi.begin(9600);  // Arduino to serial monitor
}

void loop()
{
    // Get 10 sample value from the sensor for smooth the value
    for(int i=0;i<10;i++)       
    { 
        buf[i]=analogRead(sensorPin);
        delay(10);
    }

    // Sort the analog from small to large
    for(int i=0;i<9;i++)
    {
        for(int j=i+1;j<10;j++)
        {
            if(buf[i]>buf[j])
            {
                temp=buf[i];
                buf[i]=buf[j];
                buf[j]=temp;
            }
        }
    }

    // Take the average value of 6 center sample
    avgValue=0;
    for(int i = 2; i < 8; i++)                      
    {
        avgValue+=buf[i];
    }
    
    // Convert the analog into millivolt
    float phValue = (float) avgValue * 5.0 / 1024 / 6; 

    // Convert the millivolt into pH value
    phValue = 3.5 * phValue;   

    // Send  data to Raspberry Pi
    serialPi.print("<");
    serialPi.print(phValue, DEC);
    serialPi.println(">");  

    // Wait for 5 seconds
    delay(5000);
}