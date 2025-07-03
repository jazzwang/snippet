import argparse
from icalendar import Calendar

def read_file_to_string(input_filename):
    with open(input_filename, 'r') as file:
        return file.read()

def main():
    parser = argparse.ArgumentParser(description="Process an iCal file.")
    parser.add_argument('input_file', type=str, help='Path to the iCal file')
    
    args = parser.parse_args()
    
    ical_data = read_file_to_string(args.input_file)
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

if __name__ == "__main__":
    main()
