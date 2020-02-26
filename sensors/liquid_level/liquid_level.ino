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

const int liquid_level_sensor_pin = 5;        //added
int liquid_level = 0;

void setup() {
    Serial.begin(9600);
    pinMode(liquid_level_sensor_pin, INPUT);
}

void loop() {
    liquid_level = digitalRead(5);
    Serial.print("liquid_level= ");
    Serial.println(liquid_level, DEC);
    delay(500);
}
