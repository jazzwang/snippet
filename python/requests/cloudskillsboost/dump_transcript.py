#!/usr/bin/env python3
# coding: utf-8
"""Downloads and prints transcripts from Cloud Skills Boost learning paths."""

import json
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.cloudskillsboost.google"

def extract_transcript(video_url):
    """Extracts the transcript from a given video URL."""
    try:
        response = requests.get(video_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.text, "lxml")
        transcript_data = json.loads(soup.find('ql-youtube-video').attrs["transcript"])
        transcript_lines = [item["text"] for item in transcript_data]
        return " ".join(transcript_lines)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching transcript: {e}")
        return None

def main():
    path_id = 9
    learn_paths_url = f"{BASE_URL}/paths/{path_id}"
    try:
        learn_paths_response = requests.get(learn_paths_url)
        learn_paths_response.raise_for_status()
        soup = BeautifulSoup(learn_paths_response.text, "lxml")
        course_hrefs = soup.find_all('a', {"class": 'activity-link'})
        course_links = [f"{BASE_URL}{url.get('href')}" for url in course_hrefs]

        for course_link in course_links:
            try:
                course_response = requests.get(course_link)
                course_response.raise_for_status()
                outline = json.loads(BeautifulSoup(course_response.text, "lxml").find('ql-course-outline').attrs["modules"])
                hrefs = []
                for section in outline:
                    for step in section.get("steps"):
                        hrefs.append(step.get("activities")[0].get("href"))

                video_urls = [href for href in hrefs if href and 'video' in href]
                all_transcripts = []
                for href in video_urls:
                    video_url = f"{BASE_URL}{href}"
                    transcript = extract_transcript(video_url)
                    if transcript:
                        all_transcripts.append(transcript)

                for transcript in all_transcripts:
                    print(transcript)

            except requests.exceptions.RequestException as e:
                print(f"Error fetching course: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching learning paths: {e}")


if __name__ == "__main__":
    main()
