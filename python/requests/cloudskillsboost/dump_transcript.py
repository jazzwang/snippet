# coding: utf-8
import json
import requests
from bs4 import BeautifulSoup

base_url = "https://www.cloudskillsboost.google"
path_id = 9
learn_paths = requests.get(base_url + "/paths/" + str(path_id))
course_hrefs = BeautifulSoup(learn_paths.text,"lxml").find_all('a', {"class": 'activity-link'})
course_links = [ base_url + url.get("href") for url in course_hrefs ]
for course_link in course_links:
    course = requests.get(course_link)
    outline = json.loads(BeautifulSoup(course.text, "lxml").find('ql-course-outline').attrs["modules"])
    hrefs = []
    for section in outline:
        for step in section.get("steps"):
            hrefs.append(step.get("activities")[0].get("href"))
    
    video_urls = [ href for href in hrefs if href and 'video' in href ]
    for href in video_urls:
        video = requests.get("https://www.cloudskillsboost.google" + href)
        transcripts = json.loads(BeautifulSoup(video.text, "lxml").find('ql-youtube-video').attrs["transcript"])
        srt = [ text["text"] for text in transcripts ]
        print(" ".join(string for string in srt))