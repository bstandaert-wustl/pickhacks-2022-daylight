'''
Author: Yifei Li
Date: 2022-04-09 09:13:00
LastEditTime: 2022-04-09 11:43:41
FilePath: /pickhacks-22/led.py
'''
import RPi.GPIO as GPIO

class RGB_LED:
    def __init__(self, R_PIN, G_PIN, B_PIN):
        GPIO.setmode(GPIO.BOARD)
        self.R_PIN = R_PIN
        self.G_PIN = G_PIN
        self.B_PIN = B_PIN

        GPIO.setup(R_PIN, GPIO.OUT)
        GPIO.output(R_PIN, GPIO.LOW)
        GPIO.setup(G_PIN, GPIO.OUT)
        GPIO.output(G_PIN, GPIO.LOW)
        GPIO.setup(B_PIN, GPIO.OUT)
        GPIO.output(B_PIN, GPIO.LOW)

        self.brightness = 100
        
        self.r = 255
        self.g = 255
        self.b = 255

        self.pwm_r = GPIO.PWM(R_PIN, 100)
        self.pwm_g = GPIO.PWM(G_PIN, 100)
        self.pwm_b = GPIO.PWM(B_PIN, 100)

        self.pwm_r.start(self.brightness)
        self.pwm_g.start(self.brightness)
        self.pwm_b.start(self.brightness)
    
    def set_RGB(self, R, G, B, bright):
        self.r = R
        self.g = G
        self.b = B
        self.brightness = bright

        self.pwm_r.ChangeDutyCycle(self.r / 255 * self.brightness)
        self.pwm_g.ChangeDutyCycle(self.g / 255 * self.brightness)
        self.pwm_b.ChangeDutyCycle(self.g / 255 * self.brightness)

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

    def __del__(self):
        self.pwm_r.stop()
        self.pwm_g.stop()
        self.pwm_b.stop()
        

