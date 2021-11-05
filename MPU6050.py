# Implementation file for the MPU6050
# Gyroscopic Sensor
# Class will be written to pull Gyroscopic
# values from peripheral.

# Class will be written so other drives
# can be called with similiar process.

import smbus
import math
import time


# Constant Definitions
AD0_0 = 0x68
ACCEL_CONFIG = 0x1C

# Acceleration constants
ACCEL_2G = 2
ACCEL_2G_REG_VALUE = 0

ACCEL_4G = 4
ACCEL_4G_REG_VALUE = 8

ACCEL_8G = 8
ACCEL_8G_REG_VALUE = 16

ACCEL_16G = 16
ACCEL_16G_REG_VALUE = 24

PWR_MGMT_REG_1_ADDR = 0x6B
PWR_MGMT_REG_2_ADDR = 0x6C

X_ACCL_H_ADDR = 0x3B
Y_ACCL_H_ADDR = 0x3D
Z_ACCL_H_ADDR = 0x3F

X_ACCL_L_ADDR = 0x3C
Y_ACCL_L_ADDR = 0x3E
Z_ACCL_L_ADDR = 0x40


# Class Definition
class MPU6050:

    # device_address = AD0_0
    # accel_full_scale = 2
    # bus = 0

    # Constrictor
    def __init__(self, AD0, ACCEL_FS, ACCEL_RV):
        self.device_address = AD0
        # Setting instance config for full scale acceleration
        self.accel_full_scale = ACCEL_FS
        self.accel_reg_val = ACCEL_RV

        self.bus = smbus.SMBus(1)  # Open the I2C Bus on I2C device 1
        self.bus.write_byte_data(self.device_address, PWR_MGMT_REG_1_ADDR, 0)
        self.bus.write_byte_data(self.device_address, ACCEL_CONFIG, self.accel_reg_val)

        # Configure chip to use selected full scale settings

    # Reads the Z acceleration registers and returns the
        # Z acceleration value in Gs.
    def read_z_acceleration(self):
        h = self.bus.read_byte_data(self.device_address, Z_ACCL_H_ADDR)
        l = self.bus.read_byte_data(self.device_address, Z_ACCL_L_ADDR)
        value = (h << 8) + l    # Combining into 16-bit

        # Convert from unsigned 16-bit to signed 16-bit
        if (value >= 0x8000):
            value = -((65535 - value) + 1)

        # Sclaing for full scale
        return ((self.accel_full_scale/(65536/2)) * value)

    def read_x_acceleration(self):
        h = self.bus.read_byte_data(self.device_address, X_ACCL_H_ADDR)
        l = self.bus.read_byte_data(self.device_address, X_ACCL_L_ADDR)
        value = (h << 8) + l    # Combining into 16-bit

        # Convert from unsigned 16-bit to signed 16-bit
        if (value >= 0x8000):
            value = -((65535 - value) + 1)

        # Sclaing for full scale
        return ((self.accel_full_scale/(65536/2)) * value)

    def read_y_acceleration(self):
        h = self.bus.read_byte_data(self.device_address, Y_ACCL_H_ADDR)
        l = self.bus.read_byte_data(self.device_address, Y_ACCL_L_ADDR)
        value = (h << 8) + l    # Combining into 16-bit

        # Convert from unsigned 16-bit to signed 16-bit
        if (value >= 0x8000):
            value = -((65535 - value) + 1)

        # Sclaing for full scale
        return ((self.accel_full_scale/(65536/2)) * value)
