#include <Wire.h>
#include <BleMouse.h>
#include <MPU6050.h>
#include <Arduino.h>

//Need to make the mouse to respond only to changes ?

constexpr int IR_SENSOR_PIN = 33;  // ADC pin (Analog to Digital Converter) for reading the IR sensor
constexpr int LED = 2;     // Built-in LED is connected to GPIO 2
constexpr int LEFT_CLICK_THRESHOLD = 1000;
constexpr int RIGHT_CLICK_THRESHOLD =2000;

BleMouse bleMouse;
MPU6050 mpu;

void setup() {
  Serial.begin(115200);
  Wire.begin();

  // Initialize MPU6050
  mpu.initialize();
  if (!mpu.testConnection()) {
    Serial.println("Failed to connect to MPU6050.");
    while (1);
  }
  Serial.println("MPU6050 connected!");

  // Initialize BLE Mouse
  Serial.println("Starting BLE Mouse...");
  bleMouse.begin();
}

void loop() {
  if (bleMouse.isConnected()) {
    // Read accelerometer data
    int analogValue = analogRead(IR_SENSOR_PIN);
    if(analogValue>=LEFT_CLICK_THRESHOLD && analogValue<RIGHT_CLICK_THRESHOLD){
      bleMouse.press(MOUSE_LEFT);
      delay(100);
      bleMouse.release(MOUSE_LEFT);
    }
    else if(analogValue>=RIGHT_CLICK_THRESHOLD){
      bleMouse.press(MOUSE_RIGHT);
      delay(100);
      bleMouse.release(MOUSE_RIGHT);
    }
    int16_t ax, ay, az;
    mpu.getAcceleration(&ax, &ay, &az);

    // Map accelerometer data to mouse movement with increased range
    float sensitivityMultiplier = 3.5;
    int xMove = map(ax, -17000, 17000, -10, 10) * sensitivityMultiplier;
    int yMove = map(ay, -17000, 17000, -10, 10) * sensitivityMultiplier;

    // Lowered sensitivity threshold for more movement
    int sensitivityThreshold = 4000;
    if (abs(ax) > sensitivityThreshold || abs(ay) > sensitivityThreshold) {
      bleMouse.move(xMove, yMove);
      Serial.print("Mouse Move X: "); Serial.print(xMove);
      Serial.print(" Y: "); Serial.println(yMove);
    } else {
      Serial.println("In dead zone, no movement");
    }

    delay(50);
  } else {
    Serial.println("BLE Mouse not connected");
    delay(1000);
  }
}
