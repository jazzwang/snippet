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
        video_element = soup.find('ql-youtube-video')
        if video_element:
            transcript_data = json.loads(video_element.attrs["transcript"])
            transcript_lines = [item["text"] for item in transcript_data]
            return " ".join(transcript_lines)
        else:
            return None
    except (requests.exceptions.RequestException, json.JSONDecodeError, KeyError) as e:
        print(f"Error processing transcript for {video_url}: {e}")
        return None

import argparse

def get_video_urls_from_course(course_link):
    try:
        course_response = requests.get(course_link)
        course_response.raise_for_status()
        outline_element = BeautifulSoup(course_response.text, "lxml").find('ql-course-outline')
        if outline_element:
            try:
                outline = json.loads(outline_element.attrs["modules"])
                hrefs = []
                for section in outline:
                    for step in section.get("steps", []):  # Handle missing "steps"
                        for activity in step.get("activities", []): # Handle missing "activities"
                            href = activity.get("href")
                            if href:
                                hrefs.append(href)
                return hrefs
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error processing course outline for {course_link}: {e}")
                return []
        else:
            print(f"Could not find 'ql-course-outline' element in {course_link}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching course: {e}")
        return []


def main():
    parser = argparse.ArgumentParser(description="Download transcripts from Cloud Skills Boost learning paths.")
    parser.add_argument("path_id", type=int, help="The ID of the learning path.")
    parser.add_argument("--output", "-o", help="Output file to save transcripts (default: print to stdout)")
    args = parser.parse_args()

    path_id = args.path_id
    learn_paths_url = f"{BASE_URL}/paths/{path_id}"
    try:
        learn_paths_response = requests.get(learn_paths_url)
        learn_paths_response.raise_for_status()
        soup = BeautifulSoup(learn_paths_response.text, "lxml")
        course_hrefs = soup.find_all('a', {"class": 'activity-link'})
        course_links = [f"{BASE_URL}{url.get('href')}" for url in course_hrefs]

        for course_link in course_links:
            hrefs = get_video_urls_from_course(course_link)
            video_urls = [href for href in hrefs if href and 'video' in href]
            all_transcripts = []
            for href in video_urls:
                video_url = f"{BASE_URL}{href}"
                transcript = extract_transcript(video_url)
                if transcript:
                    all_transcripts.append(transcript)

            if args.output:
                with open(args.output, "w") as f:
                    for transcript in all_transcripts:
                        f.write(transcript + "\n")
            else:
                for transcript in all_transcripts:
                    print(transcript)


    except requests.exceptions.RequestException as e:
        print(f"Error fetching learning paths: {e}")


if __name__ == "__main__":
    main()
