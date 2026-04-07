# Reflection — Hsinchu School Zone Lookup

> **Note:** This feedback is AI-generated and experimental. It's meant to surface useful observations, not to grade you. Take what resonates, ignore what doesn't. Your own sense of what you learned matters more than anything here.

## Scope & Idea Clarity

**What went well:** The scope clearly identified the user's problem — parents needing to look up school zones from complex PDFs. The decision to use search/select kept the project feasible within the time constraint. Clear evidence in `docs/scope.md`.

**What to try next time:** Consider more specific user research — maybe interview 1-2 actual parents to understand their pain points better (e.g., do they know their 里 name?).

## Requirements Thinking

**What went well:** The PRD captured the core user stories well: search → village → neighborhood → school. The distinction between "entire village" vs "partial neighborhood assignments" was a key insight that shaped the data model.

**What to try next time:** The PRD noted the data would be "manually extracted from PDF" but didn't plan for verification time. Next time, allocate explicit time for data accuracy checking.

## Technical Decisions

**What went well:** Chose Vanilla JS with no dependencies — exactly right for a single-file project that runs locally without a build step. The Google-style search pattern is intuitive and maintainsable. Evidence in `docs/spec.md`.

**What to try next time:** Consider a more scalable data format earlier. The initial dropdown-based design worked but was improved with search.

## Plan vs. Reality

**What went well:** The checklist's 9 items mapped well to actual implementation. Data extraction (step 1) did take the most time, as expected. The build completed without major blockers.

**What to try next time:** The PDF extraction step was harder than anticipated because the PDF had complex table layout. Next time, search for machine-readable data (CSV/JSON) before committing to PDF extraction.

## How You Worked

**What went well:** Good collaboration during `/scope` — you answered questions clearly about the target user and desired UI. The decision to iterate and improve the UI (from dropdowns to Google-style search) showed good judgment.

**What to try next time:** More proactive pushback during requirements discussion would deepen learning. For example, asking "what if a parent doesn't know their 里 name?" could lead to interesting features.

## Your Goals

You came in wanting to learn "vibe coding" — how to articulate what you want clearly to AI. Throughout this process, you got practice describing requirements, seeing how they translated into code, and making tradeoffs. The spec-driven approach forced you to be explicit about what "done" looks like, which is exactly the skill vibe coding requires.

## Iteration Summary

The project went through 6 iteration cycles that improved the app significantly:
1. Fixed UI: hide 鄰 dropdown when not needed
2. Added search: real-time 里 filtering  
3. Added source links: education bureau + PDF
4. Added contact info: address/phone display
5. Mobile polish: responsive CSS
6. Redesign: Google-style search (major improvement — removed confusing district dropdown)

## Milestone Completion

- /scope: complete
- /prd: complete
- /spec: complete
- /checklist: complete
- /build: 9/9 checklist items completed
- /iterate: 6 iteration cycles
- /reflect: complete
