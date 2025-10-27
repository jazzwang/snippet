```bash
~/Downloads$ cat gcp-cloudskillsboost-list.txt | awk -F';' '{ print $1 " | " $2 }' | sed 's#https://www.cloudskillsboost.google/paths/##' | sort -n | awk -F'|' 'BEGIN { print "| path_id | title |\n|---|---|" } { print "| " $1 " | " $2 " |" }' | tee ~/git/snippet/md/gcp/cloudskillsboost/cloudskillsboost-list.md
```

| path_id | title |
|---|---|
| 8  |  Getting Started with Google Cloud Learning Path |
| 9  |  Cloud Digital Leader Learning Path |
| 11  |  Cloud Engineer Learning Path |
| 12  |  Cloud Architect Learning Path |
| 13  |  Hybrid and Multi-Cloud Architect Learning Path |
| 14  |  Network Engineer Learning Path |
| 15  |  Security Engineer Learning Path |
| 16  |  Data Engineer Learning Path |
| 17  |  Machine Learning Engineer Learning Path |
| 18  |  Data Analyst Learning Path |
| 19  |  Cloud Developer Learning Path |
| 20  |  DevOps Engineer, SRE Learning Path |
| 21  |  API Developer Learning Path |
| 22  |  Database Engineer Learning Path |
| 23  |  Workspace End User Learning Path |
| 24  |  Google Workspace Administrator Learning Path |
| 27  |  Cloud Architect/Engineer on Apigee |
| 28  |  BI and Analytics with Looker |
| 30  |  AppSheet Developer Learning Path |
| 31  |  Startup Innovators Learning Path  |
| 32  |  Google Cloud Next 2022 Hands-On Labs |
| 36  |  Google Cloud Computing Foundations Certificate |
| 71  |  Google Cloud Infrastructure for AWS professionals |
| 72  |  Google Cloud Infrastructure for Azure  professionals |
| 76  |  DevSecOps Learning Path |
| 108  |  IT Heroes Summit learning path |
| 110  |  Public Sector Learning Path |
| 118  |  Beginner: Introduction to Generative AI Learning Path |
| 125  |  Cloud Architect Accelerated Learning Path for AWS professionals |
| 126  |  Cloud Architect Accelerated Learning Path for Azure professionals |
| 183  |  Advanced: Generative AI for Developers Learning Path |
| 184  |  Google Cloud Next 2023 Learning Path |
| 187  |  Google SIEM & SOAR Learning Path |
| 236  |  Gemini for Google Cloud Learning Path |
| 249  |  Gemini for Google Workspace |
| 280  |  Google Cloud Applied AI Summit Learning Path  |
| 371  |  Public Preview |
| 419  |  Beginner: Google Cloud Cybersecurity Certificate |
| 420  |  Beginner: Google Cloud Data Analytics Certificate |
| 516  |  Google Cloud Next 2024 Learning Path |
| 581  |  Google Security Operations |
| 655  |  Vertex AI Search for Retail |
| 708  |  Contact Center AI (CCAI) Platform |
| 1281  |  Integrate Generative AI Into Your Data Workflow |
| 1282  |  Build and Modernize Applications With Generative AI |
| 1283  |  Deploy and Manage Generative AI Models |
| 1284  |  Generate Smarter Generative AI Outputs |
| 1336  |  Associate Data Practitioner Learning Path |
| 1547  |  GDC Air-Gapped Security Operator Fundamentals |
| 1551  |  GDC Air-Gapped Practitioner Fundamentals |
| 1803  |  Gemini in BigQuery |
| 1834  |  Professional Cloud Architect Renewal Exam Learning Path |
| 1839  |  Network Security Learning Path |
| 1858  |  Google Cloud Next 2025 |
| 1872  |  Intermediate: Generative AI Labs with Gemini on Google Cloud |
| 1873  |  Advanced: Generative AI Labs with Gemini on Google Cloud |
| 1951  |  Generative AI Leader |
| 2150  |  Security Operations Engineer Learning Path |
| 2480  |  AI Boost Bites: Your Edge in the AI-Powered World |
| 2806  |  Google Cloud AI Infrastructure |
