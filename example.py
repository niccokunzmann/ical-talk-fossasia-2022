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

## Ical file from test cases
url = "http://tinyurl.com/y24m3r8f"
date = (2019, 3) # March 2019

## German Holidays
url = "https://www.calendarlabs.com/ical-calendar/ics/46/Germany_Holidays.ics"
date = 2022 # year 2022

## FOSSASIA 2022 events
# from https://api.eventyay.com/v1/events/6b901f56.ics?include_sessions
url = "https://niccokunzmann.github.io/ical-talk-fossasia-2022/summit.ics"
date = (2022, 4, 8, 12) # midday at the 8th of April 2022

ical_string = urlopen(url).read()
calendar = icalendar.Calendar.from_ical(ical_string)
events = recurring_ical_events.of(calendar).at(date)
for event in events:
    print("start {} summary {}".format(event["DTSTART"].dt, event.get("SUMMARY")))
