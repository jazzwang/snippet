#!/usr/bin/env python3
# coding: utf-8
"""Downloads and prints transcripts from Cloud Skills Boost learning paths."""

import json
import requests
import argparse
import google.generativeai as genai
from google.api_core import retry
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# Load GOOGLE_API_KEY from .env
load_dotenv()

# Create the Gemini model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="""Tasks:\n
        1. Translate the input into Traditional Chinese\n
        2. Use concise and precise tone to convert input into bullet points in Traditional Chinese. \n\n
        Output format:\n\n
        > {output of task #1}\n\n
        ##### 摘要\n\n
        {output of task #2}\n\n
    """,
)
# Create retry policy
retry_policy = {"retry": retry.Retry(predicate=retry.if_transient_error)}

BASE_URL = "https://www.cloudskillsboost.google"

def get_course_context(course_url):
    try:
        course_response = requests.get(course_url)
        course_response.raise_for_status()
        return BeautifulSoup(course_response.text, "lxml")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching course: {e}")
        exit(1)

def get_course_title(soup, course_url):
    """Extracts the course title from the BeautifulSoup object.

    Args:
        soup: The BeautifulSoup object representing the course page.
        course_url: The URL of the course.

    Returns:
        The course title as a string, or None if not found.

    Raises:
        ValueError: If the 'ql-title-medium' element is not found.
    """
    course_title = soup.find_all('h2', {"class": "ql-title-medium"})
    if course_title:
        return course_title[0].text + ": " + course_title[1].text.replace("\n", "")
    else:
        raise ValueError(f"Could not find 'ql-title-medium' element in {course_url}")

def get_course_modules(soup, course_url):
    """Extracts course modules from the BeautifulSoup object.

    Args:
        soup: The BeautifulSoup object representing the course page.
        course_url: The URL of the course.

    Returns:
        A list of course modules, or None if not found.

    Raises:
        ValueError: If the 'ql-course-outline' element or "modules" attribute is not found.
        JSONDecodeError: If the modules data is not valid JSON.
    """
    outline_element = soup.find('ql-course-outline')
    if outline_element:
        try:
            outline = json.loads(outline_element.attrs["modules"])
            return outline
        except (json.JSONDecodeError, KeyError) as e:
            raise type(e)(f"Error processing course outline for {course_url}: {e}") from e
    else:
        raise ValueError(f"Could not find 'ql-course-outline' element in {course_url}")

def get_activities(module):
    """Extracts activities from a module.

    Args:
        module: A dictionary representing a module.

    Returns:
        A list of tuples, where each tuple contains (activity_title, activity_type, activity_url).
    """
    activities = []
    for step in module.get("steps", []):
        for activity in step.get("activities", []):
            activity_title = activity.get("title")
            activity_url = activity.get("href")
            activity_type = activity.get("type")

            if activity_title is not None and activity_url is not None and activity_type is not None:
                activities.append((activity_title, activity_type, activity_url))
    return activities

def extract_transcript(video_url):
    """Extracts the transcript from a given video URL.

    Args:
        video_url: The URL of the video.

    Returns:
        The transcript as a string, or None if an error occurs or the transcript is not found.
    """
    try:
        response = requests.get(video_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")
        video_element = soup.find('ql-youtube-video')
        if video_element:
            try:
                transcript_data = json.loads(video_element.attrs["transcript"])
                if transcript_data:
                    transcript_lines = [item["text"] for item in transcript_data]
                    return " ".join(transcript_lines)
                else:
                    return None  # Or handle empty transcript data differently
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error extracting transcript data for {video_url}: {e}")
                return None
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching video for {video_url}: {e}")
        return None

def translate_transcript(transcript):
    # translate and convert input into bullet points
    response = model.generate_content(transcript, request_options=retry_policy)
    print(response.text)

def main():
    # parsing CLI arguments
    parser = argparse.ArgumentParser(description="Download transcripts from Cloud Skills Boost learning paths.")
    parser.add_argument("path_id", type=int, help="The ID of the learning path.")
    parser.add_argument("--translate", "-t", help="Output translation and summary generated by Gemini 1.5 Flash)")
    args = parser.parse_args()

    path_id = args.path_id
    learn_paths_url = f"{BASE_URL}/paths/{path_id}"

    try:
        # 1. Get Learning Path Title and Course URLs
        learn_paths_response = requests.get(learn_paths_url)
        learn_paths_response.raise_for_status()
        soup = BeautifulSoup(learn_paths_response.text, "lxml")
        learning_plan_title = soup.find('h1',{"class":"learning-plan-title"}).text

        print(f"# {learning_plan_title}\n")
        print(f"- {learn_paths_url}\n")
        print(f"[TOC]\n")

        course_urls = [f"{BASE_URL}{url.get('href')}" for url in soup.find_all('a', {"class": 'activity-link'})]

        # 2. Get Course Title and Modules
        for course_url in course_urls:
            soup = get_course_context(course_url)
            course_title = get_course_title(soup, course_url)
            print(f"## {course_title}\n")
            print(f"- {course_url}\n")

            modules = get_course_modules(soup, course_url)

            # 3. Get Module Title and Activities
            for module in modules:
                module_title = module["title"]
                print(f"### {module_title}\n")
                # 4. Get Activity Title, Type and URL
                activities = get_activities(module)
                for (activity_title, activity_type, activity_url) in activities:
                    print(f"#### {activity_title}\n")
                    video_url = f"{BASE_URL}{activity_url}"
                    print(f"- {video_url}\n")
                    ## Only extract transcript if type is "video"
                    if activity_type == "video":
                        transcript = extract_transcript(video_url)
                        if transcript:
                            print(f"{transcript}\n")
                            if args.translate:
                                translate_transcript(transcript)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching learning paths: {e}")

if __name__ == "__main__":
    main()
