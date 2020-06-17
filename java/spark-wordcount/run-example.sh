#!/bin/bash
spark-submit --class JavaWordCount build/libs/spark-wordcount-java.jar settings.gradle
