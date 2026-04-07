# Hsinchu School Zone Lookup

## Idea
A single-page web application that lets parents in Hsinchu City search for their 里 (village) and 鄰 (neighborhood), and displays which junior high school their child should attend.

## Who It's For
Parents of elementary school children in Hsinchu City who need to look up their child's assigned junior high school based on their residential address.

## Inspiration & References
- Hsinchu City Education Bureau School Zone Query: https://www.hc.edu.tw/edub/basic/schoolArea.aspx
- 114 Academic Year Junior High School Zone Map (PDF): https://www.hc.edu.tw/edub/basic/schoolarea/114jh.pdf
- Taiwan Government Open Data - Village Boundary Maps: https://data.gov.tw/dataset/7438
- Design: Clean, simple, mobile-friendly — focus on usability for parents

## Goals
- Simple search-based UI — search for 里 → select → see school
- Display the assigned junior high school name clearly
- Single HTML file for easy local execution

## What "Done" Looks Like
A single HTML file that can be opened directly in a browser. The user:
1. Types a 里 name in the search box
2. Selects from autocomplete results
3. Optionally selects a 鄰 (if the 里 has partial assignment)
4. Sees the assigned school(s) displayed

## What's Explicitly Cut
- Interactive map — using search/select instead
- Address lookup by typing — only search by 里 name
- Mobile-responsive optimization — basic usability only
- Data API integration — embedding data directly in JS

## Loose Implementation Notes
- Use Vanilla JS (no build step)
- Embed school zone data as JSON in the JS file
- Use Google-style autocomplete search for 里 names
