from ics import Calendar
import requests
import arrow

url = "https://calendar.google.com/calendar/ical/f7ejnn7bs80n91vr0nm8v5jbg4%40group.calendar.google.com/private-ad9b307842f33f3d7c36b3c9e522e922/basic.ics"
c = Calendar(requests.get(url).text)

for e in c.timeline:
    print(e.begin)
e = list(c.timeline)[0]
"Event '{}' started {}".format(e.name, e.begin.humanize())

def getCurrentEvent():
    now = arrow.now()
    for e in c.timeline:
        if now > e.begin and now < e.end:
            return e

