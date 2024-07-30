#include <WiFi.h>
#include <WebServer.h>
#include <ESP32Servo.h>

const char *ssid = "";              // Replace with your network SSID
const char *password = ""; // Replace with your network password

WebServer server(80);
Servo servo1;       // Create servo1 object
Servo servo2;       // Create servo2 object
int servoPin1 = 13; // Pin where servo1 is connected
int servoPin2 = 12; // Pin where servo2 is connected

void handleRoot()
{
    server.send(200, "text/plain", "Hello from ESP32 Servo Controller!");
}

void handleServo()
{
    if (server.hasArg("angle1") && server.hasArg("angle2"))
    {
        String angle1 = server.arg("angle1");
        String angle2 = server.arg("angle2");
        int servoAngle1 = angle1.toInt();
        int servoAngle2 = angle2.toInt();

        if ((servoAngle1 >= 0 && servoAngle1 <= 180) && (servoAngle2 >= 0 && servoAngle2 <= 180))
        {
            servo1.write(servoAngle1);
            servo2.write(servoAngle2);
            server.sendHeader("Access-Control-Allow-Origin", "*");
            server.send(200, "text/plain", "Servo angles set to " + angle1 + " and " + angle2);
        }
        else
        {
            server.sendHeader("Access-Control-Allow-Origin", "*");
            server.send(400, "text/plain", "Invalid angles. Must be between 0 and 180.");
        }
    }
    else
    {
        server.sendHeader("Access-Control-Allow-Origin", "*");
        server.send(400, "text/plain", "Angles not provided.");
    }
}

void setup()
{
    // Initialize serial communication at 115200 bits per second:
    Serial.begin(115200);

    // Set up WiFi
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("Connected to WiFi");
    Serial.println(WiFi.localIP());

    // Attach the servos to the specified pins
    servo1.attach(servoPin1);
    servo2.attach(servoPin2);

    // Set up the web server routes
    server.on("/", handleRoot);
    server.on("/servo", handleServo);

    server.begin();
    Serial.println("HTTP server started");
}

void loop()
{
    server.handleClient();
}
