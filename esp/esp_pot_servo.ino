#include <ESP32Servo.h>

Servo myServo;     // Create a servo object
int potPin = 32;   // Pin where the potentiometer is connected
int servoPin = 13; // Pin where the servo is connected

void setup()
{
    // Initialize serial communication at 115200 bits per second:
    Serial.begin(115200);

    // Set the resolution to 12 bits (0-4095)
    analogReadResolution(12);

    // Attach the servo to the specified pin
    myServo.attach(servoPin);
}


void loop()
{
    // Read the analog value from the potentiometer
    int analogValue = analogRead(potPin);

    // Map the analog value (0-4095) to the servo angle (0-180)
    int servoAngle = map(analogValue, 0, 4095, 0, 180);

    // Set the servo position
    myServo.write(servoAngle);

    // Print out the values
    Serial.printf("ADC analog value = %d\n", analogValue);
    Serial.printf("Servo angle = %d\n", servoAngle);

    delay(100); // Delay in between reads for clear output
}
