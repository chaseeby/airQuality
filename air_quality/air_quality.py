import time
import board
import busio
from adafruit_pm25.i2c import PM25_I2C

reset_pin = None
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
pm25 = PM25_I2C(i2c, reset_pin)

def get_air_quality():
    try:
        aqdata = pm25.read()
        return {
            "pm10_standard": aqdata["pm10 standard"],
            "pm25_standard": aqdata["pm25 standard"],
            "pm100_standard": aqdata["pm100 standard"],
            "pm10_env": aqdata["pm10 env"],
            "pm25_env": aqdata["pm25 env"],
            "pm100_env": aqdata["pm100 env"],
            "particles_03um": aqdata["particles 03um"],
            "particles_05um": aqdata["particles 05um"],
            "particles_10um": aqdata["particles 10um"],
            "particles_25um": aqdata["particles 25um"],
            "particles_50um": aqdata["particles 50um"],
            "particles_100um": aqdata["particles 100um"]
        }
    except RuntimeError:
        return None