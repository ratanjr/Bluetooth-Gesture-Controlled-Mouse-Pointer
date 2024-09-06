import smbus
import time

# MPU-6050 Registers
MPU6050_ADDR = 0x68  # MPU-6050 device address
PWR_MGMT_1 = 0x6B    # Power management register
ACCEL_XOUT_H = 0x3B  # Accelerometer data register

# Initialize the I2C bus
bus = smbus.SMBus(1)  # I2C bus 1

# Function to read raw data from a register
def read_raw_data(addr):
    # Read two consecutive bytes from the address
    high = bus.read_byte_data(MPU6050_ADDR, addr)
    low = bus.read_byte_data(MPU6050_ADDR, addr + 1)
    # Combine the two bytes and handle the sign bit (16-bit two's complement)
    value = (high << 8) | low
    if value > 32768:
        value = value - 65536
    return value

# Wake up the MPU-6050 as it starts in sleep mode
bus.write_byte_data(MPU6050_ADDR, PWR_MGMT_1, 0)

try:
    while True:
        # Read accelerometer data
        accel_x = read_raw_data(ACCEL_XOUT_H)
        accel_y = read_raw_data(ACCEL_XOUT_H + 2)
        accel_z = read_raw_data(ACCEL_XOUT_H + 4)

        # Convert raw values to 'g' units (gravity)
        Ax = accel_x / 16384.0
        Ay = accel_y / 16384.0
        Az = accel_z / 16384.0

        print(f"Ax={Ax:.2f} g, Ay={Ay:.2f} g, Az={Az:.2f} g")

        time.sleep(1)

except KeyboardInterrupt:
    print("Program terminated")
