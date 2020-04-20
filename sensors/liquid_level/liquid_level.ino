/* Adapted from example by Vasoo Veerapen  
 https://www.instructables.com/member/VasooV/ */

#define sensorPin 5

// Raspberry Pi is connected to Serial 0
#define serialPi Serial

void setup() {
    serialPi.begin(9600);  // Arduino to serial monitor
    pinMode(sensorPin, INPUT);
}

void loop() {
    // Read sensor data
    // int sensorData = DHT.read11(sensorPin);
    // float temperature = DHT.temperature;
    // float humidity = DHT.humidity;
    int liquid_level = digitalRead(sensorPin);

    // Send  data to Raspberry Pi
    serialPi.print("<liquid_level=");
    serialPi.print(liquid_level);
    serialPi.println(">");
    
    // Wait for 5 seconds
    delay(5000);
}