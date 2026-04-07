# Process Notes

## /onboard
Learner: Jazz Wang. Intermediate level, familiar with AI coding tools (Gemini CLI, Aider). Goal: learn vibe coding — how to articulate what they want clearly.

## /scope
- Project: 新竹里別查學區 (single-page web app)
- Target users: 新竹市國小學童家長
- UI: Dropdown/tree selector ( District → 里 → 鄰)
- Data: Will embed 學區 data directly (PDF not machine-readable)
- Tech: Single HTML with CDN JS, Vanilla JS

## /prd
- Product: 新竹里別查學區 (dropdown-based school zone lookup)
- User stories: District selector, 里 selector, 鄰 selector (conditional), school result display
- Data: Will embed 114學年度 data manually from PDF as JSON
- Non-goals: No map, no geocoding, no address input (dropdown only)
- Open question: 115學年度 data available, but PDF format — using 114 for now

## /spec
- Stack: Vanilla HTML/JS/CSS, no build tools, no dependencies
- Architecture: Single file with UI/Logic/Data layers
- Data: Embedded JSON structure matching PDF 里鄰 format
- Key decisions: Cascading dropdowns, handle 共同學區

## /checklist
- Build mode: Step-by-step with comprehension checks
- 9 items total, data extraction is step 1 (most time-consuming)
- Final step is Devpost submission

