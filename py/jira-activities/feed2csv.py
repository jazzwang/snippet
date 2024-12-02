import feedparser
import sys

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " Username")
    exit(1)
else:
    user_id = sys.argv[1]

json_file = open(user_id + ".json","w+")
csv_file = open(user_id + ".csv","w+")
d=feedparser.parse(user_id + ".xml")
print(d,file=json_file)
for i in d['entries']:
    timestamp=i['published']
    print(i['id'] + ";" + i['link'] + ";" + i['title'] + ";" + i['published'] + ";" + i['activity_verb'], file=csv_file)
