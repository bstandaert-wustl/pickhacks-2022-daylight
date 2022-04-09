'''
Author: Yifei Li
Date: 2022-04-09 10:17:01
LastEditTime: 2022-04-09 10:30:48
FilePath: /用所选项目新建的文件夹/testled.py
'''
from led import RGB_LED as RGB

led1 = RGB.__init__(11, 13, 15)

led1.set_color('red')
led1.set_brightness(50)
led1.set_brightness(100)
led1.set_brightness(50)
led1.set_color('green')

led1.set_RGB(100, 200, 300, 100)

led1.set_RGB(300, 200, 100)