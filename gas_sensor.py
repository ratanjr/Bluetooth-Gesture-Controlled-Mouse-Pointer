import RPi.GPIO as GPIO
import time

# Define the physical pin where the FC-22 sensor is connected
sensor_pin = 11  # Physical pin 11 (GPIO 17)
led_pin = 12     # Physical pin 12 (GPIO 18) for LED (optional)

# Set up the GPIO using physical pin numbering
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor_pin, GPIO.IN)  # Set sensor pin as input
GPIO.setup(led_pin, GPIO.OUT)    # Set LED pin as output (for indication)

try:
    while True:
        # Read the sensor value (HIGH or LOW)
        if GPIO.input(sensor_pin):
            print("No gas detected")
            GPIO.output(led_pin, GPIO.LOW)  # Turn off LED (optional)
        else:
            print("Gas detected!")
            GPIO.output(led_pin, GPIO.HIGH)  # Turn on LED (optional)
        
        time.sleep(0.5)  # Wait half a second before reading again

except KeyboardInterrupt:
    # Clean up GPIO settings on exit
    GPIO.cleanup()
    print("Program stopped by user")
