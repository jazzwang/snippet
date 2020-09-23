import feedparser
feedparser.parse("evans_ye.xml")
json_file = open("evans_ye.json","w+")
csv_file = open("evans_ye.csv","w+")
d=feedparser.parse("evans_ye.xml")
print(feedparser.parse("evans_ye.xml"),file=json_file)
for i in d['entries']:
    timestamp=i['published']
    print(i['id'] + ";" + i['link'] + ";" + i['title'] + ";" + i['published'] + ";" + i['activity_verb'], file=csv_file)
