'''
Author: Yifei Li
Date: 2022-04-09 10:17:01
LastEditTime: 2022-04-09 11:22:06
FilePath: /pickhacks-22/testled.py
'''
import RPi.GPIO as GPIO
from led import RGB_LED as RGB

GPIO.setmode(GPIO.BOARD)

led1 = RGB(11, 13, 15)

led1.set_color('red')
led1.set_brightness(50)
led1.set_brightness(100)
led1.set_brightness(50)
led1.set_color('green')

led1.set_RGB(100, 200, 300, 100)

led1.set_RGB(300, 200, 100)

GPIO.cleanup()