#!/bin/bash
echo "Get Job Companies ..."
python show_mbox_company.py > job_company.txt
echo "Get Job Locations ..."
python show_mbox_location.py > job_location.txt
echo "Get Job Titles ..."
python show_mbox_jobtitle.py > job_title.txt
echo "Generate CSV output"
echo "Date;company;Date2;location;Date3;title" > hadoop_jobs.csv
paste -d ";" job_company.txt job_location.txt job_title.txt >> hadoop_jobs.csv
