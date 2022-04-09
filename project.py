from ics import Calendar
import requests
import arrow
from flask import Flask, request, redirect, render_template
from apscheduler.schedulers.background import BackgroundScheduler

cal = None
calUrl = "https://calendar.google.com/calendar/ical/f7ejnn7bs80n91vr0nm8v5jbg4%40group.calendar.google.com/private-ad9b307842f33f3d7c36b3c9e522e922/basic.ics"

def loadCalendar(url):
    calUrl = url
    cal = Calendar(requests.get(url).text)

    for e in cal.timeline:
        print(e.begin, e.name)

def refreshCalendar():
    loadCalendar(calUrl)

sched = BackgroundScheduler(daemon=True)
sched.add_job(refreshCalendar,'interval',minutes=5)
sched.start()


def getCurrentEvent():
    now = arrow.now()
    for e in cal.timeline:
        if now > e.begin and now < e.end:
            return e


# server

app = Flask("smartLamp")

@app.route("/")
def show_index():
    return render_template("index.html", cal_url=calUrl)

@app.route("/update-cal")
def update_calendar_request():
    loadCalendar(request.args.get("url", ""))
    return redirect("/")


app.run(port=8080)
#app.run(port=80, host="0")