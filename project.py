from ics import Calendar
import requests
import arrow
from flask import Flask, request, redirect, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from led import RGB_LED as RGB
import datetime
from cal import *

led1 = RGB(11, 13, 15)

led1.set_debug(True)

def updateLEDs():
    rgb = (50, 0, 0, 100)
    print(getCurrentEvent())
    if getCurrentEvent() is not None:
        rgb = (255, 0, 0, 100)
    print(rgb)
    led1.set_RGB(rgb[0], rgb[1], rgb[2], rgb[3])

sched = BackgroundScheduler(daemon=True)
sched.add_job(updateLEDs, 'interval', seconds=5)
sched.start()
# server

app = Flask("smartLamp")

@app.route("/")
def show_index():
    return render_template("index.html", cal_url=calUrl, time=getCurrentTime().format("YYYY-MM-DD HH:mm:ss ZZ"))

@app.route("/update-cal")
def update_calendar_request():
    loadCalendar(request.args.get("url", ""))
    return redirect("/")

@app.route("/update-time")
def update_time():
    global timeShift
    timeShift = arrow.utcnow() - arrow.get(request.args.get("time", ""))
    print(timeShift)
    return redirect("/")

def incrementTimeOffset():
    global timeShift
    if timeShift is None:
        timeShift = datetime.timedelta(seconds=100)
    else:
        timeShift -= datetime.timedelta(seconds=100)

@app.route("/enable-fast-time")
def enableFastTime():
    timeSched = BackgroundScheduler(daemon=True)
    timeSched.add_job(incrementTimeOffset,'interval',seconds=1)
    timeSched.start()
    return redirect("/")

#app.run(port=8080)
app.run(port=8000, host="0")