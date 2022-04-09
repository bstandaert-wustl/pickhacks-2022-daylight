'''
Author: Yifei Li
Date: 2022-04-09 09:13:00
LastEditTime: 2022-04-09 09:41:49
FilePath: /undefined/Users/liyifei/Downloads/led
'''
import RPi.GPIO as GPIO

class RGB_LED:
    def __init__(self, R_PIN, G_PIN, B_PIN):
        self.R_PIN = R_PIN
        self.G_PIN = G_PIN
        self.B_PIN = B_PIN

        GPIO.setmode(GPIO.BOARD)

        brightness = 100
        
        self.r = 255
        self.g = 255
        self.b = 255

        pwm_r = GPIO.PWM(R_PIN, 100)
        pwm_g = GPIO.PWM(G_PIN, 100)
        pwm_b = GPIO.PWM(B_PIN, 100)

        pwm_r.start(brightness)
        pwm_g.start(brightness)
        pwm_b.start(brightness)
    
    def set_RGB(self, R, G, B, bright):
        self.r = R
        self.g = G
        self.b = B
        self.brightness = bright

        self.pwm_r.changeDutyCycle(self.r / 255 * 100 * self.brightness)
        self.pwm_g.changeDutyCycle(self.g / 255 * 100 * self.brightness)
        self.pwm_b.changeDutyCycle(self.g / 255 * 100 * self.brightness)

    def set_brightness(self, bright):
        self.brightness = bright
        self.set_RGB(self.r, self.g, self.b, self.brightness)

    # color literal to rgb value
    def set_color(self, color):
        if color == 'red':
            self.r = 255
            self.g = 0
            self.b = 0
            self.set_RGB(self.r, self.g, self.b, self.brightness)

        elif color == 'green':
            self.r = 0
            self.g = 255
            self.b = 0
            self.set_RGB(self.r, self.g, self.b, self.brightness)

        elif color == 'blue':
            self.r = 0
            self.g = 0
            self.b = 255
            self.set_RGB(self.r, self.g, self.b, self.brightness)

        elif color == 'yellow':
            self.r = 255
            self.g = 255
            self.b = 0
            self.set_RGB(self.r, self.g, self.b, self.brightness)

        elif color == 'cyan':
            self.r = 0
            self.g = 255
            self.b = 255
            self.set_RGB(self.r, self.g, self.b, self.brightness)

        elif color == 'magenta':
            self.r = 255
            self.g = 0
            self.b = 255
            self.set_RGB(self.r, self.g, self.b, self.brightness)

        elif color == 'white':
            self.r = 255
            self.g = 255
            self.b = 255
            self.set_RGB(self.r, self.g, self.b, self.brightness)

        elif color == 'black':
            self.r = 0
            self.g = 0
            self.b = 0
            self.set_RGB(self.r, self.g, self.b, self.brightness)

        else:
            self.set_RGB(self.r, self.g, self.b, self.brightness)
