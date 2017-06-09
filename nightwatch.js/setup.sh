#!/bin/bash
## Reference:
## https://hackernoon.com/node-js-end-to-end-testing-with-nightwatch-js-1c11163d442c

SELENIUM_URL=http://selenium-release.storage.googleapis.com/3.4
SELENIUM_JAR=selenium-server-standalone-3.4.0.jar
mkdir -p bin
if [ ! -d node_modules ]; then
  npm install nightwatch --save-dev
fi
if [ ! -f bin/selenium-server-standalone.jar ]; then
  wget -O bin/selenium-server-standalone.jar $SELENIUM_URL/$SELENIUM_JAR
fi

if [ ! -f bin/chromedriver ]; then
  (
    cd bin;
    wget https://chromedriver.storage.googleapis.com/2.30/chromedriver_mac64.zip
    unzip chromedriver_mac64.zip
  )
fi


