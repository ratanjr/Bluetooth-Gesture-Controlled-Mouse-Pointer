import RPi.GPIO as GPIO
import time

# Set up the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define the pin connected to the IR sensor DO pin
DO_PIN = 11  # GPIO17 corresponds to pin 11 in BOARD mode

# Set up the DO pin as input
GPIO.setup(DO_PIN, GPIO.IN)

try:
    while True:
        # Read the digital value from the IR sensor
        if GPIO.input(DO_PIN) == 0:
            print("Object detected!")
        else:
            print("No object detected.")
        
        # Add a small delay to avoid flooding the console with messages
        time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped by user.")

finally:
    # Clean up GPIO settings before exiting
    GPIO.cleanup()
