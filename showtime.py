#!env python3

# 1. Generate an image
# 2. Sleep for 60 seconds
# 3. Repeat

import time
import datetime
import board
import busio
from adafruit_bme280 import Adafruit_BME280
from adafruit_bme280 import Adafruit_BME280_I2C

import inkyphat
import sys
from PIL import ImageFont

# We will not hit the remote weatber server every minute,
weather_interval=15
weather_countdown=0

um how do I do a class in python again ah,,,, been doing only JavaScript lately
class Weather:

    def _init_(self) :
        self.currentTemperature   = 72
        self.currentWindSpeed     = 0
        self.currentWindDirection = 'NW'
        return

    def get(self):
        return status

w = Weather()

while(1):
    if weather_countdown <= 0:
        w.get()
        weather_interval = weather_countdown

    # generate clock face

    if pi():
        # push image to Inky
    else:
        # serve image via web browser

    # sleep 60 seconds
