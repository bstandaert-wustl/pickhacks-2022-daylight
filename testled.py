'''
Author: Yifei Li
Date: 2022-04-09 10:17:01
LastEditTime: 2022-04-09 11:51:26
FilePath: /pickhacks-22/testled.py
'''
import RPi.GPIO as GPIO
import time
from led import RGB_LED as RGB

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

led1 = RGB(11, 13, 15)
time.sleep(0.5)
led1.set_color('red')
time.sleep(0.5)

led1.set_brightness(50)
time.sleep(0.5)

led1.set_brightness(100)
time.sleep(0.5)

led1.set_brightness(50)
time.sleep(0.5)

led1.set_color('green')
time.sleep(0.5)

led1.set_RGB(100, 200, 255, 100)
time.sleep(0.5)

led1.set_RGB(255, 200, 100, 100)
time.sleep(0.5)

GPIO.cleanup()