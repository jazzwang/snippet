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