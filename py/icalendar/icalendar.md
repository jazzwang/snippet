# icalendar

## 2025-07-03

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
are there python library that can read ical file and show the detailed invitation description?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, there are excellent Python libraries that can read iCalendar (ICS) files and extract detailed invitation descriptions and other event information. The most popular and well-regarded ones are:

1.  **`icalendar`**: This is a robust and widely used library for parsing and generating iCalendar files (RFC 5545 compliant). It allows you to:

      * Read an ICS file (or string).
      * Iterate through calendar components like `VCALENDAR`, `VEVENT`, `VTODO`, etc.
      * Access properties of events, such as `SUMMARY` (event title), `DESCRIPTION` (detailed invitation description), `DTSTART`, `DTEND`, `LOCATION`, `ORGANIZER`, `ATTENDEE`, and more.
      * Handle recurring events (RRULE, RDATE, EXDATE).

    **How to get the description:**
    Once you parse the iCal file and get an `Event` object, you can usually access the description using `event.get('description')` or `event['description']`.

2.  **`ics.py`**: This library aims to provide a more "pythonic" and user-friendly interface for working with iCalendar data. It's built on top of the iCalendar specification and offers convenient ways to read and write ICS data.

    **How to get the description:**
    With `ics.py`, after loading a calendar, you can access events through `calendar.events`. Each `Event` object will have a `description` attribute (e.g., `event.description`).

**Example using `icalendar`:**

```python
from icalendar import Calendar, Event

# Assume you have an iCal file named 'invitation.ics'
# Or you can read from a string if the iCal data is in memory
ical_data = """
BEGIN:VCALENDAR
PRODID:-//Example Corp//NONSGML Event Generator//EN
VERSION:2.0
BEGIN:VEVENT
UID:19970901T130000Z-123405@example.com
DTSTAMP:19970901T130000Z
DTSTART:20250710T090000Z
DTEND:20250710T100000Z
SUMMARY:Important Meeting
DESCRIPTION:This is a detailed description of the meeting.
 This will cover project updates, next steps, and action items.
 Please come prepared with your progress reports.
LOCATION:Conference Room A
ORGANIZER;CN=John Doe:mailto:john.doe@example.com
ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-PARTICIPANT;PARTSTAT=NEEDS-ACTION;RSVP=
 TRUE;CN=Alice Smith:mailto:alice.smith@example.com
ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=OPT-PARTICIPANT;PARTSTAT=NEEDS-ACTION;RSVP=
 TRUE;CN=Bob Johnson:mailto:bob.johnson@example.com
END:VEVENT
END:VCALENDAR
"""

cal = Calendar.from_ical(ical_data)

for component in cal.walk():
    if component.name == "VEVENT":
        summary = component.get('summary')
        description = component.get('description')
        dtstart = component.decoded('dtstart')
        dtend = component.decoded('dtend')
        location = component.get('location')
        organizer = component.get('organizer')
        attendees = component.get('attendee')

        print(f"Event Summary: {summary}")
        print(f"Description: {description}")
        print(f"Start Time: {dtstart}")
        print(f"End Time: {dtend}")
        print(f"Location: {location}")
        print(f"Organizer: {organizer}")
        if attendees:
            print("Attendees:")
            if isinstance(attendees, list):
                for att in attendees:
                    print(f"  - {att.params.get('CN', str(att))}")
            else:
                 print(f"  - {attendees.params.get('CN', str(attendees))}")
        print("-" * 30)

```

This example demonstrates how to extract various details, including the `DESCRIPTION` field, which contains the detailed invitation description. Remember to install the library first using `pip install icalendar`.
</td></tr></table>

- 複製範例程式到 `icalendar-example.py` 並安裝 `pip install icalendar`
- 實測：
```bash
~/git/snippet/py/icalendar$ python icalendar-example.py 
Event Summary: Important Meeting
Description: This is a detailed description of the meeting.This will cover project updates, next steps, and action items.Please come prepared with your progress reports.
Start Time: 2025-07-10 09:00:00+00:00
End Time: 2025-07-10 10:00:00+00:00
Location: Conference Room A
Organizer: mailto:john.doe@example.com
Attendees:
  - Alice Smith
  - Bob Johnson
------------------------------
```

## 2025-08-26

- 發現 icalendar 套件有自帶 CLI 工具：
```bash
~/git/snippet/py/icalendar$ which icalendar
/c/Users/jazzw/scoop/apps/python/current/Scripts/icalendar
```
```bash
~/Downloads/ics$ icalendar.exe
usage: icalendar [-h] [--output OUTPUT] [-v] calendar_files [calendar_files ...]
icalendar: error: the following arguments are required: calendar_files
~/Downloads/ics$ icalendar.exe 20259.ics
    Organizer:
    Attendees:

    Summary    : 2025年9月份天下會員讀書會
    Starts     : Tue Sep  9 12:30:00 2025
    End        : Tue Sep  9 13:30:00 2025
    Duration   : 1:00:00
    Location   :
    Comment    :
    Description:
     領讀書籍： 《閱讀空氣懂人心》
     領讀人： 奧美公關/奧美集團董事總經理 謝馨慧
     時間： 9 月 9 日（週五）12:30~13:30
```
- 從錯誤訊息可以知道程式來自套件 `icalendar` 的 `cli.py`
```
FileNotFoundError: [Errno 2] No such file or directory: 'Azure'
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\jazzw\scoop\apps\python\current\Scripts\icalendar.exe\__main__.py", line 7, in <module>
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\icalendar\cli.py", line 96, in main
    with open(calendar_file, encoding="utf-8-sig") as f:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```
