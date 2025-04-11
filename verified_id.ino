#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX (Arduino to ESP32)
const int ledPin = 8; // LED connected to digital pin 8

void setup() {
    Serial.begin(9600);      // Serial Monitor
    mySerial.begin(9600);    // Communication with ESP32

    pinMode(ledPin, OUTPUT);
    digitalWrite(ledPin, HIGH); // LED stays ON initially

    delay(2000); // Allow time for ESP32 to initialize
    mySerial.println("ARDUINO-002"); // Send Device ID
}

void loop() {
    if (mySerial.available()) {
        String response = mySerial.readStringUntil('\n'); // Read response from ESP32
        response.trim(); // Remove extra spaces and newline characters
        Serial.println("HUB response: [" + response + "]");

        if (response.equals("Not Authorized")) {
            blinkLED(); // Start blinking if unauthorized
        } else if (response.equals("Authorized")) {
            digitalWrite(ledPin, HIGH); // Keep LED ON if authorized
        }
    }
    delay(3000);
}

void blinkLED() {
    Serial.println("🔴 Unauthorized! Blinking LED...");
    for (int i = 0; i < 15; i++) { // Blink LED 5 times
        digitalWrite(ledPin, LOW);
        delay(500);
        digitalWrite(ledPin, HIGH);
        delay(500);
    }
}