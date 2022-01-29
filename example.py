"""Example file to use with recurring_ical_events for FOSSASIA 2022

To prepare:
- install Python3 and pip
- run this in the command line:
    python3 -m pip install recurring-ical-events

You can find the talk at:
    https://niccokunzmann.github.io/ical-talk-fossasia-2022
If you like to view the repository or recurring_ical_events:
    https://github.com/niccokunzmann/python-recurring-ical-events

"""
import icalendar, recurring_ical_events
from urllib.request import urlopen
ical_string = urlopen("http://tinyurl.com/y24m3r8f").read()
calendar = icalendar.Calendar.from_ical(ical_string)
events = recurring_ical_events.of(calendar).at((2022, 3))
for event in events:
    print("start {} summary {}".format(event["DTSTART"].dt, event.get("SUMMARY")))