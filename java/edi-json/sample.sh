#!/bin/bash
wget -O edi-json.jar https://github.com/BerryWorksSoftware/edi-json/raw/master/repo/com/berryworks/edireader-json-basic/5.5.19/edireader-json-basic-5.5.19.jar
wget https://raw.githubusercontent.com/BerryWorksSoftware/edi-json/master/Sample824.edi
java -jar edi-json.jar Sample824.edi Sample824.json
