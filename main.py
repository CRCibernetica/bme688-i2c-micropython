from machine import Pin,I2C
from roboboard import RoboBoard
from time import sleep_ms
from bme688 import *

i2c = I2C(0, sda=Pin(21), scl=Pin(22))

sensor = BME680_I2C(i2c)

while True:
    gas = sensor.gas
    temperature = sensor.temperature
    humidity = sensor.humidity
    pressure = sensor.pressure
    print(f'Temp: {temperature:.1f}C,  RH: {humidity:.1f}%,  Pressure: {pressure:.1f}kPa,  Gas: {gas:.1f}ppm')
    sleep_ms(5000)