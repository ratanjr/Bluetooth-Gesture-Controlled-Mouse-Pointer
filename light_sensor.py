import RPi.GPIO as GPIO
import time

# Define the physical pins where the LM393 sensor and LED are connected
sensor_pin = 11  # Physical pin 11 (GPIO 17)
led_pin = 12     # Physical pin 12 (GPIO 18) for LED

# Set up the GPIO using physical pin numbering
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor_pin, GPIO.IN)  # Set sensor pin as input
GPIO.setup(led_pin, GPIO.OUT)    # Set LED pin as output

try:
    while True:
        # Read the sensor value (HIGH or LOW)
        if GPIO.input(sensor_pin):
            print("No Light detected")
            GPIO.output(led_pin, GPIO.HIGH)  # Turn on LED
        else:
            print("light detected")
            GPIO.output(led_pin, GPIO.LOW)   # Turn off LED
        
        time.sleep(0.5)  # Wait half a second before reading again

except KeyboardInterrupt:
    # Clean up GPIO settings on exit
    GPIO.cleanup()
    print("Program stopped by user")
