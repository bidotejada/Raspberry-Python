# Utilizes the MPU6050 class to call
# acceleration values from Gyro Chip

from MPU6050 import *
import math
import time

sensor = MPU6050(AD0_0, ACCEL_2G, ACCEL_2G_REG_VALUE)
sensor_1 = MPU6050(AD0_0, ACCEL_8G, ACCEL_8G_REG_VALUE)

while True:
    print(f'x_accel: {sensor.read_x_acceleration()}')
    print(f'y_accel: {sensor.read_y_acceleration()}')
    print(f'z_accel: {sensor.read_z_acceleration()}\n')
    time.sleep(0.5)

    print(f'x_accel: {sensor_1.read_x_acceleration()}')
    print(f'y_accel: {sensor_1.read_y_acceleration()}')
    print(f'z_accel: {sensor_1.read_z_acceleration()}\n')
    time.sleep(0.5)
