from ics import Calendar
import requests
import arrow
from flask import Flask, request, redirect, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from led import RGB_LED as RGB

led1 = RGB(11, 13, 15)

led1.set_debug(True)

def updateLEDs():
    rgb = (50, 0, 0, 100)
    print(getCurrentEvent())
    if getCurrentEvent() is not None:
        rgb = (255, 0, 0, 100)
    print(rgb)
    led1.set_RGB(rgb[0], rgb[1], rgb[2], rgb[3])

cal = None
calUrl = "https://calendar.google.com/calendar/ical/f7ejnn7bs80n91vr0nm8v5jbg4%40group.calendar.google.com/private-ad9b307842f33f3d7c36b3c9e522e922/basic.ics"

timeShift = None

def getCurrentTime():
    print(timeShift)
    if timeShift:
      return arrow.utcnow() - timeShift
    else:
        return arrow.utcnow()

def loadCalendar(url):
    global cal
    global calUrl
    calUrl = url
    cal = Calendar(requests.get(url).text)

    for e in cal.timeline:
        print(e.begin, e.name)

def refreshCalendar():
    loadCalendar(calUrl)

loadCalendar(calUrl)

sched = BackgroundScheduler(daemon=True)
sched.add_job(refreshCalendar,'interval',minutes=5)
sched.add_job(updateLEDs, 'interval', seconds=5)
sched.start()


def getCurrentEvent():
    now = getCurrentTime()
    for e in cal.timeline:
        print(e.name, e.begin, e.end, now)
        if now > e.begin and now < e.end:
            return e


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


#app.run(port=8080)
app.run(port=8000, host="0")