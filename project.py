from ics import Calendar
import requests
import arrow
from flask import Flask, request, redirect, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from led import RGB_LED as RGB
import datetime
from cal import *
import time

led1 = RGB(3, 5, 7)
led2 = RGB(11, 13, 15)
led3 = RGB(19, 21, 23)
led4 = RGB(29, 31, 33)
led1.set_debug(True)
led2.set_debug(True)
led3.set_debug(True)
led4.set_debug(True)

def setAllLED(rgb):
    led1.set_RGB(rgb[0], rgb[1], rgb[2], rgb[3])
    led2.set_RGB(rgb[0], rgb[1], rgb[2], rgb[3])
    led3.set_RGB(rgb[0], rgb[1], rgb[2], rgb[3])
    led4.set_RGB(rgb[0], rgb[1], rgb[2], rgb[3])


def updateLEDs():
    print(getCurrentEvent(), getPrevEventInDay(), getNextEventInDay())
    rgb = (255, 255, 200, 100)

    if getPrevEventInDay() is None and getNextEventInDay() and getNextEventInDay().begin - getCurrentTime() < datetime.timedelta(hours=0.5):
        #1st event is starting
        rgb = (200, 200, 255, 100)

    elif getNextEventInDay() and getNextEventInDay().begin - getCurrentTime() < datetime.timedelta(minutes=4):
        #event is starting now
        for i in range(4):
            rgb = (255, 0, 0, 100)
            setAllLED(rgb)
            time.sleep(0.5)
            rgb = (0, 255, 0, 100)
            setAllLED(rgb)
            time.sleep(0.5)
            rgb = (0, 0, 255, 100)
            setAllLED(rgb)
            time.sleep(0.5)

    elif getCurrentEvent() is not None:
        rgb = (0, 255, 0, 100)

    elif getCurrentEvent() is None and (getPrevEventInDay() is None or getNextEventInDay() is None):
        #events for today are not started or done
        rgb = (255, 0, 0, 100)

    print(rgb)
    setAllLED(rgb)

sched = BackgroundScheduler(daemon=True)
sched.add_job(updateLEDs, 'interval', seconds=1)
sched.start()
# server

app = Flask("smartLamp")

@app.route("/")
def show_index():
    return render_template("index.html", cal_url=calUrl, time=getCurrentTime().to("US/Central").format("YYYY-MM-DD HH:mm:ss ZZ"), timeShift=getTimeShift())

@app.route("/update-cal")
def update_calendar_request():
    loadCalendar(request.args.get("url", ""))
    return redirect("/")

@app.route("/update-time")
def update_time():
    setTimeShift(arrow.utcnow() - arrow.get(request.args.get("time", "")))
    return redirect("/")

def incrementTimeOffset():
    if getTimeShift() is None:
        setTimeShift(datetime.timedelta(seconds=100))
    else:
        setTimeShift(getTimeShift() - datetime.timedelta(seconds=100))

@app.route("/enable-fast-time")
def enableFastTime():
    timeSched = BackgroundScheduler(daemon=True)
    timeSched.add_job(incrementTimeOffset,'interval',seconds=1)
    timeSched.start()
    return redirect("/")

#app.run(port=8080)
app.run(port=8000, host="0")