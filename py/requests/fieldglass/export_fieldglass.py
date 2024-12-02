import re
import json
import getpass
import requests
from bs4 import BeautifulSoup

username = input("FieldGlass ID: ")
password = getpass.getpass("Password: ")

base_url = "https://www.fieldglass.net"
session = requests.Session()
session.headers["User-Agent"]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
r1 = session.get(base_url)
r1.raise_for_status()

### /login.do

login_data = {
    "language": "en_US",
    "qalogin" : "null",
    "username": username,
    "password": password,
    "action": "Sign In",
    "next": "/worker_desktop.do",
    "_for": "",
    "_company_code": "",
    "_resource_id": "",
    "_destination": "",
    "_destination_context": "",
    "client_width": 1440,
    "client_height": 790,
    "flash_enabled": "false",
    "noBrowserCheck": "true",
    "isCookieEnabled": "true"
}

r2 = session.post(base_url + "/login.do", login_data)
r2.raise_for_status()

### https://www.fieldglass.net/time_sheet_list.do?cf=1
r3 = session.get(base_url + "/time_sheet_list.do?cf=1")

pattern = r"^\{.*\"maxRowCountReached\":"
timesheet_meta = [line for line in r3.text.splitlines() if re.match(pattern, line)]
data = json.loads(timesheet_meta[0])
records = [ column for row in data["rows"] for column in row["columns"] if column["name"] == "time_sheet_ref" ]
timesheet_links = [ re.split('"',record["html"])[3] for record in records ]
timesheet_links.reverse()
for i in range(len(timesheet_links)):
    r5 = session.get(timesheet_links[i])
    r5.raise_for_status()

    soup = BeautifulSoup(r5.text, "lxml")
    table = soup.find('table',id="timeSheetMainTable")

    dates = [ th.text[:-3] for th in table.find_all(class_="dateAndDay") ]
    hours = [ td.text for total in table.find_all('tr',class_="timeSheetTotal") for td in total.find_all('td') ]

    for index in range(0,7):
        print(f"{dates[index]},{hours[index]}")
