# caldav

- 緣起：
  - 想自動化產生 Confluence Calendar 的 Event

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
are there RESTful API of confluence to create calendar event?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
While Confluence offers REST APIs for general content management (pages, spaces, etc.), a dedicated, officially documented REST API for directly creating **Team Calendar events** isn't as straightforward or universally available across all Confluence versions (Cloud, Server, Data Center).

Here's a breakdown of the situation:

* **No Direct Official Confluence REST API for Team Calendar Events:** Atlassian's main Confluence REST API (for content like pages and spaces) does not explicitly include endpoints for creating, editing, or deleting Team Calendar events. This has been a long-standing feature request in the Atlassian community.

* **Workarounds and Unofficial Endpoints:**
    * **CalDAV API:** Confluence Team Calendars supports the **CalDAV protocol**. This means you can use CalDAV clients or libraries to interact with Confluence calendars. CalDAV is a standardized way to access scheduling information on a remote server, and it can be used for creating and retrieving calendar details and events. 
    * **Undocumented/Internal Endpoints:** Some community threads and third-party tools suggest using internal or "undocumented" REST endpoints that the Confluence UI itself uses to create calendar events. These typically look like `/rest/calendar-services/1.0/calendar/events.json` and involve specific JSON payloads. However, these are **not officially supported** and can change without notice in future Confluence updates, potentially breaking your integrations.
    * **Third-Party Add-ons/Integrations:** For specific Confluence versions (like Data Center), there might be third-party apps or integrations that expose their own REST APIs for calendar event management. For example, "Company Calendar for Jira" mentions a REST API for creating and editing events.
    * **Python Wrappers:** There are community-contributed Python wrappers (like `confluence-calendar-api` on PyPI) that attempt to simplify interactions with these less-documented calendar APIs.

* **Feature Requests and Ongoing Discussions:** There are active feature requests on Atlassian's Jira platform (e.g., CONFSERVER-51696, CONFCLOUD-51696) for a formal REST API to manipulate Team Calendar events. This indicates that it's a desired feature but not yet officially implemented in the main REST API.

**In summary:**

If you need to programmatically create calendar events in Confluence, your best bets are:

* **Leveraging the CalDAV API:** This is the most "official" and supported method for interacting with Team Calendars programmatically. It might require more understanding of CalDAV itself.
* **Using caution with unofficial REST endpoints:** If you choose to use the `rest/calendar-services` endpoints, be aware that they are not officially supported and may be subject to change. Test thoroughly with each Confluence upgrade.
* **Exploring third-party add-ons:** Check the Atlassian Marketplace for Confluence add-ons that specifically offer a documented REST API for their calendar functionalities.

Always refer to the official Atlassian Developer documentation for the most up-to-date and supported REST API information for your specific Confluence version (Cloud, Server, or Data Center).
</td></tr></table>

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you give me a python example to leveraging confluence CalDAV API to create a new event?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, you can leverage the Confluence CalDAV API to create a new event using Python. The most convenient way to do this is by using a CalDAV client library like `caldav`.

Here's a Python example that demonstrates how to create a new event in a Confluence Team Calendar using the `caldav` library.

**Prerequisites:**

1.  **Install the `caldav` library:**
    ```bash
    pip install caldav icalendar
    ```
2.  **Confluence CalDAV URL:** You'll need the CalDAV URL for your specific Confluence Team Calendar. You can usually find this by going to your Confluence calendar, clicking "Subscribe," and selecting "CalDAV." The URL will look something like `https://your-confluence-url/plugins/servlet/team-calendars/caldav/<calendar-ID>`.
3.  **Confluence Username and Password (or API Token):** You'll need valid credentials to authenticate with Confluence. For Confluence Cloud, it's recommended to use an API token. For Confluence Server/Data Center, you can use your username and password or a personal access token.

<!-- end list -->

```python
import caldav
from datetime import datetime, timedelta
import pytz # For timezone handling

# --- Configuration ---
CONFLUENCE_URL = "https://your-confluence-instance.com"  # Your Confluence base URL
CALDAV_PATH = "/plugins/servlet/team-calendars/caldav/<calendar-ID>" # The CalDAV path for your specific calendar
USERNAME = "your_confluence_username"  # Your Confluence username
PASSWORD = "your_confluence_password_or_api_token" # Your Confluence password or API token

# Ensure you replace <calendar-ID> with the actual ID from your Confluence calendar's CalDAV URL.
# Example: If your CalDAV URL is https://confluence.example.com/plugins/servlet/team-calendars/caldav/12345,
# then CALDAV_PATH would be "/plugins/servlet/team-calendars/caldav/12345"

# --- Event Details ---
event_summary = "Team Meeting 🚀"
event_description = "Discuss Q3 planning and project updates."
event_location = "Meeting Room A"
event_start = datetime(2025, 8, 22, 10, 0, 0, tzinfo=pytz.timezone('Asia/Taipei')) # August 22, 2025, 10:00 AM, Taiwan time
event_end = datetime(2025, 8, 22, 11, 0, 0, tzinfo=pytz.timezone('Asia/Taipei'))   # August 22, 2025, 11:00 AM, Taiwan time

# --- Create Event ---
def create_confluence_calendar_event():
    try:
        # Construct the full CalDAV URL for the calendar
        caldav_url = f"{CONFLUENCE_URL}{CALDAV_PATH}"

        print(f"Connecting to CalDAV URL: {caldav_url}")

        # Create a CalDAV client
        client = caldav.DAVClient(url=caldav_url, username=USERNAME, password=PASSWORD)

        # Get the principal (user's calendar account)
        principal = client.principal()
        if not principal:
            print("Failed to get CalDAV principal. Check URL and credentials.")
            return

        # Get the specific calendar.
        # Confluence Team Calendars typically expose one calendar per calendar ID.
        # We'll try to get the first calendar associated with the principal and the given URL.
        calendars = principal.calendars()
        target_calendar = None
        for calendar in calendars:
            if calendar.url.path.strip('/') == CALDAV_PATH.strip('/'):
                target_calendar = calendar
                break
        
        if not target_calendar:
            print(f"Could not find calendar with path: {CALDAV_PATH}. Ensure the path is correct and the user has access.")
            print("Available calendars:")
            for cal in calendars:
                print(f" - {cal.url.path}")
            return

        print(f"Found calendar: {target_calendar.url}")

        # Create the event
        new_event = target_calendar.save_event(
            dtstart=event_start,
            dtend=event_end,
            summary=event_summary,
            description=event_description,
            location=event_location
        )
        print(f"Event created successfully! URL: {new_event.url}")

    except caldav.lib.error.DAVError as e:
        print(f"CalDAV error occurred: {e}")
        print("Please check your Confluence URL, CalDAV path, username, and password/API token.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    create_confluence_calendar_event()
```

-----

### How it works:

1.  **Import necessary libraries:**

      * `caldav`: The Python library for interacting with CalDAV servers.
      * `datetime`, `timedelta`: For handling dates and times.
      * `pytz`: For proper timezone handling, which is crucial for calendar events.

2.  **Configuration:**

      * `CONFLUENCE_URL`: Your Confluence instance's base URL (e.g., `https://mycompany.atlassian.net` for Cloud or `https://confluence.yourdomain.com/confluence` for Server/Data Center with a context path).
      * `CALDAV_PATH`: The specific path to your Confluence Team Calendar via CalDAV. You **must** get this from your Confluence calendar's "Subscribe" option, choosing "CalDAV." It typically includes a unique ID.
      * `USERNAME` and `PASSWORD`: Your Confluence login credentials. For Confluence Cloud, use an API token as the password.

3.  **Event Details:** Define the `summary`, `description`, `location`, `start` time, and `end` time for your new event. **Important:** Always include timezone information for `datetime` objects using `pytz.timezone`.

4.  **`caldav.DAVClient`:** This initializes the CalDAV client with your Confluence URL and credentials.

5.  **`client.principal()`:** This method retrieves the "principal" object, which represents the authenticated user's calendar account on the server.

6.  **`principal.calendars()`:** This gets a list of all calendars accessible by the principal. We then iterate through them to find the specific calendar that matches our `CALDAV_PATH`.

7.  **`target_calendar.save_event()`:** This is the core function. It takes the event details (`dtstart`, `dtend`, `summary`, etc.) and creates the event on the Confluence Team Calendar. The `caldav` library handles the conversion to iCalendar (`.ics`) format and sends the appropriate HTTP PUT request.

8.  **Error Handling:** The `try-except` block catches potential `caldav.lib.error.DAVError` (for CalDAV-specific issues like authentication or invalid URLs) and other general exceptions.

-----

### Before running:

  * **Replace placeholders:** Make sure to replace `your-confluence-instance.com`, `your_confluence_username`, `your_confluence_password_or_api_token`, and especially `<calendar-ID>` with your actual Confluence details.
  * **Timezones:** Be mindful of timezones. Always specify `tzinfo` for your `datetime` objects to avoid unexpected scheduling issues.
  * **Permissions:** Ensure the Confluence user associated with the `USERNAME` has **write access** to the specified Team Calendar.
  * **Confluence Version:** While CalDAV support is a standard feature of Team Calendars, always check your specific Confluence version's documentation for any nuances or requirements.

This example provides a solid foundation for programmatically creating events in Confluence Team Calendars via their CalDAV API.
</td></tr></table>