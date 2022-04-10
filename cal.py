from ics import Calendar
import requests
import arrow
from flask import Flask, request, redirect, render_template
from apscheduler.schedulers.background import BackgroundScheduler
import datetime

cal = None
calUrl = "https://calendar.google.com/calendar/ical/f7ejnn7bs80n91vr0nm8v5jbg4%40group.calendar.google.com/private-ad9b307842f33f3d7c36b3c9e522e922/basic.ics"

timeShift = None

def setTimeShift(ts):
    global timeShift
    timeShift = ts

def getTimeShift():
    return timeShift

def getCurrentTime():
    print("ts", timeShift)
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
sched.start()


def getCurrentEvent():
    now = getCurrentTime()
    for e in cal.timeline:
        if now > e.begin and now < e.end:
            return e

def getPrevEventInDay():
    now = getCurrentTime().to("US/Central")
    prev = None
    for e in cal.timeline:
        #print(e.name, e.begin, e.end, now)
        if (e.begin < now and (prev is None or e.begin > prev.begin)):
            prev = e
    if prev is None or now.floor("day") != prev.begin.to("US/Central").floor("day"):
        return None
    return prev

def getNextEventInDay():
    now = getCurrentTime().to("US/Central")
    next = None
    for e in cal.timeline:
        #print(e.name, e.begin, e.end, now)
        if (e.begin > now and (next is None or e.begin < next.begin)):
            next = e
    if next is None or now.floor("day") != next.begin.to("US/Central").floor("day"):
        return None
    return next