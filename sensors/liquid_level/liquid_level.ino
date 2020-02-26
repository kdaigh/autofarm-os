/*********************************************************
* Liquid Level Sensor-XKC-Y25-T12V
* ********************************************************
* This example is a modified version of an original by:

* @author jackli(Jack.li@dfrobot.com)
* @version  V1.0
* @date  2016-1-30

* GNU Lesser General Public License.
* See <http://www.gnu.org/licenses/> for details.
* All above must be included in any redistribution
* ********************************************************/

#define PING 'P'
#define PING_REPLY 'A'
#define READ 'R'
#define END_CHAR 'E'

const int liquid_level_sensor_pin = 5;

void setup() 
{
    pinMode(liquid_level_sensor_pin, INPUT);
    Serial.begin(9600);
}

void loop() 
{
    // While serial port is available
    while(Serial.available() > 0)
    {
        unsigned in = Serial.read();
        switch(in)
        {
            // VERIFY WITH PI
            case PING:
                serial.write(PING REPLY);
                break;
            // READ SENSOR
            case READ:
                readSensor();
                break;
            default:
                Serial.write("Unknown command: ");
                Serial.write(in);
                break;
        }
        delay(500);
    }
}

void readLiquidLevelSensor()
{
    int liquid_level = 0;
    liquid_level = digitalRead(liquid_level_sensor_pin);
    Serial.print("liquid_level= ");
    Serial.print(liquid_level, DEC);
    Serial.println(END_CHAR);
}