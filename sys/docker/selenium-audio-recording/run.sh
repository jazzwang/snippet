#!/bin/bash
# Install dependency
npm install selenium-webdriver@^3.3.0

# Startup Selenium server
docker run --rm -d --name=grid -p 4444:24444 \
  -v $(pwd)/videos:/home/seluser/videos \
  -e VIDEO=true elgalu/selenium
docker exec grid wait_all_done 30s

# Run selenium to capture video
node record-youtube-example.js

# Save the captured video
docker exec grid stop-video
docker stop grid
