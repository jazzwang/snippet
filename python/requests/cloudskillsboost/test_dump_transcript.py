import pytest
from bs4 import BeautifulSoup
import json
import requests
from dump_transcript import (
    get_course_title,
    get_course_modules,
    get_activities,
    extract_transcript,
)

# Sample HTML content for testing
SAMPLE_HTML = """
<html>
<head></head>
<body>
    <h2 class="ql-title-medium">Course Title 1</h2>
    <h2 class="ql-title-medium">Course Title 2</h2>
    <ql-course-outline modules='[{"title": "Module 1", "steps": [{"activities": [{"title": "Activity 1", "href": "/activity1", "type": "video"}]}]}]'></ql-course-outline>
    <ql-youtube-video transcript='[{"text": "Transcript line 1"}, {"text": "Transcript line 2"}]'></ql-youtube-video>
</body>
</html>
"""

SAMPLE_HTML_NO_TRANSCRIPT = """
<html>
<head></head>
<body>
    <ql-youtube-video></ql-youtube-video>
</body>
</html>
"""

def test_get_course_title():
    soup = BeautifulSoup(SAMPLE_HTML, "lxml")
    title = get_course_title(soup, "test_url")
    assert title == "Course Title 1: Course Title 2"

    with pytest.raises(ValueError):
        soup_no_title = BeautifulSoup("<html></html>", "lxml")
        get_course_title(soup_no_title, "test_url")

def test_get_course_modules():
    soup = BeautifulSoup(SAMPLE_HTML, "lxml")
    modules = get_course_modules(soup, "test_url")
    assert modules == [{"title": "Module 1", "steps": [{"activities": [{"title": "Activity 1", "href": "/activity1", "type": "video"}]}]}]

    with pytest.raises(ValueError):
        soup_no_outline = BeautifulSoup("<html></html>", "lxml")
        get_course_modules(soup_no_outline, "test_url")

    with pytest.raises(json.JSONDecodeError):
        soup_invalid_json = BeautifulSoup('<ql-course-outline modules="invalid json"></ql-course-outline>', "lxml")
        get_course_modules(soup_invalid_json, "test_url")


def test_get_activities():
    module = {"steps": [{"activities": [{"title": "Activity 1", "href": "/activity1", "type": "video"}]}]}
    activities = get_activities(module)
    assert activities == [("Activity 1", "video", "/activity1")]

def test_extract_transcript():
    with pytest.raises(requests.exceptions.RequestException):
        extract_transcript("invalid_url")

    soup = BeautifulSoup(SAMPLE_HTML, "lxml")

    def mock_request(url):
        response = requests.Response()
        response.status_code = 200
        response._content = str.encode(SAMPLE_HTML)
        return response

    with pytest.MonkeyPatch.context() as monkeypatch:
        monkeypatch.setattr(requests, 'get', mock_request)
        transcript = extract_transcript("test_url")
        assert transcript == "Transcript line 1 Transcript line 2"

    soup_no_transcript = BeautifulSoup(SAMPLE_HTML_NO_TRANSCRIPT, "lxml")

    def mock_request_no_transcript(url):
        response = requests.Response()
        response.status_code = 200
        response._content = str.encode(SAMPLE_HTML_NO_TRANSCRIPT)
        return response

    with pytest.MonkeyPatch.context() as monkeypatch:
        monkeypatch.setattr(requests, 'get', mock_request_no_transcript)
        transcript = extract_transcript("test_url")
        assert transcript is None
