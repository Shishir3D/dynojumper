#include <Servo.h>

Servo myservo;
int motorPin = 9;  // Pin connected to the servo motor
int angle = 0;     // Initial angle of the servo motor

void setup() {
    myservo.attach(motorPin); // Attach the servo to the specified pin
    Serial.begin(9600);       // Initialize serial communication
}

void loop() {
    if (Serial.available() > 0) {
        char signal = Serial.read();  // Read the incoming signal
        
        if (signal == '1') {
            angle = 104;               // Set the angle to 90 degrees
            myservo.write(angle);     // Rotate the servo motor
           // delay(250);              // Wait for motor movement
            
            // Send response back to Python
            
        } else if (signal == '0') {
            angle = 98;                // Set the angle back to 0 degrees
            myservo.write(angle);     // Return the servo motor to initial position
        }
    }
}
