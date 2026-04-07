# Hsinchu School Zone Lookup — Product Requirements

## Problem Statement
Parents of elementary school children in Hsinchu City need to know which junior high school their child is assigned to based on their residential address (里/鄰). Currently, they must either:
1. Download and read complex PDF documents from the education bureau website
2. Call or visit the school in person

This wastes time and creates confusion during critical enrollment periods.

## User Stories

### Epic: Basic Lookup
- As a parent, I want to search for my 里 (village) so that I can find my specific neighborhood
  - [ ] Search box with autocomplete shows all matching 里
  - [ ] Results show the district (東區/北區/香山區) as a tag

- As a parent, I want to optionally select my 鄰 (neighborhood) if my 里 has partial school assignments so that I get the accurate school
  - [ ] 鄰 dropdown appears only when needed (when 里 has partial assignments)
  - [ ] Selecting a 鄰 refines the school result

- As a parent, I want to see the assigned school name clearly displayed so that I know where to enroll my child
  - [ ] Result shows school name in large, readable text
  - [ ] If multiple schools (共同學區 / shared zones), all are displayed
  - [ ] Result updates immediately when selection changes

### Epic: Error Handling
- As a parent, I want clear feedback if no school is found so that I know something is wrong
  - [ ] Display "請選擇里" prompt when no village selected
  - [ ] Show "沒有找到相符的里" when search yields no results

## What We're Building

### Core Features
1. **Google-style Search** — Single search box with autocomplete
2. **Neighborhood Selector** — Optional, appears when selected 里 has partial assignments
3. **School Result Display** — Shows assigned school name(s) prominently
4. **School Contact Info** — Address and phone number for each school

### Data Structure
- Embed 114 Academic Year junior high school zone data directly in JavaScript as JSON
- Support multiple schools per 里 or 鄰 (共同學區 / shared zones)

### Technical Implementation
- Single HTML file
- Vanilla JavaScript (no build step)
- CSS for basic styling (clean, readable)
- All data embedded in `<script>` tag

### UI Layout
```
+----------------------------------+
|         新竹里別查學區            |
+----------------------------------+
|  [搜尋新竹市里名稱...]             |
+----------------------------------+
|  [高峰里 ▼]                      |
|  [▼ 選擇] (optional)             |
+----------------------------------+
|  學區: 建華國中                   |
|  建華國中：地址 | 電話            |
+----------------------------------+
```

## What We'd Add With More Time
- Search by address input field
- Interactive map visualization
- Mobile-optimized responsive design
- School contact info with more details

## Non-Goals
- No address-to-里 geocoding — too complex for single file
- No map visualization — keeping it simple with search
- No 115 Academic Year update yet — using 114 data
- No offline PWA — single file is sufficient

## Open Questions
- Should we include 115 Academic Year data? The PDF link exists but is 114. We can update later.

## Implementation Note
The school zone data was manually extracted from the PDF and embedded as JSON. The app was redesigned mid-development to use Google-style search instead of cascading dropdowns, which better reflects how school zones are actually organized (not strictly by administrative district).
