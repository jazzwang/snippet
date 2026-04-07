# Build Checklist

## Build Preferences

- **Build mode:** Step-by-step
- **Comprehension checks:** Yes
- **Git:** Commit after each item with message: "Complete step N: [title]"
- **Verification:** Yes
- **Check-in cadence:** Learning-driven

## Checklist

- [ ] **1. Extract school zone data from PDF to JSON structure**
  Spec ref: `spec.md > Data Model`
  What to build: Manually extract all 里鄰學區 data from the 114 Academic Year PDF and format as JSON matching the spec's data model. Must include: district → village → schools (or neighborhoods → schools). Handle 共同學區 cases where multiple schools are listed.
  Acceptance: JSON object can be copy-pasted into index.html. Contains all 里 from all districts. Each 里 has at least one school assigned.
  Verify: Log the JSON to console and verify structure matches spec model.

- [ ] **2. Create HTML skeleton with search UI**
  Spec ref: `spec.md > UI Layer`
  What to build: Create index.html with basic HTML structure: header, search input, autocomplete dropdown, neighborhood select, and result div. Add basic CSS for layout.
  Acceptance: Page loads in browser. Search input visible with placeholder text.
  Verify: Open index.html in browser, confirm all UI elements render.

- [ ] **3. Embed school data in HTML**
  Spec ref: `spec.md > Data Layer`
  What to build: Insert the extracted JSON data into a `<script>` tag in index.html. Create a constant `schoolData` with the complete 114 Academic Year data.
  Acceptance: JavaScript can access `schoolData` object. Data includes all districts.
  Verify: Type `schoolData` in browser console, confirm data loads.

- [ ] **4. Implement autocomplete search logic**
  Spec ref: `spec.md > Logic Layer`
  What to build: Add event listener to search input. Filter villages as user types, show matching results with district tags. Click to select.
  Acceptance: Typing shows dropdown with matching results. Selecting updates result area.
  Verify: Test typing different 里 names, verify autocomplete works.

- [ ] **5. Implement 鄰 selector visibility logic**
  Spec ref: `spec.md > Logic Layer`
  What to build: Check if selected village has `neighborhoods` property. If yes, show neighborhood dropdown and populate with neighborhood ranges. If no, hide neighborhood dropdown.
  Acceptance: Villages with partial assignments show neighborhood dropdown. Villages without hide it.
  Verify: Select a village that has neighborhoods, confirm dropdown appears. Select one without, confirm it's hidden.

- [ ] **6. Implement school lookup and display**
  Spec ref: `spec.md > Logic Layer`
  What to build: When village (and optionally neighborhood) is selected, look up the assigned school(s) from schoolData and display in result div. Handle multiple schools (共同學區) by displaying all with contact info.
  Acceptance: Selecting a village displays the school name with address/phone. For partial assignment 里, selecting neighborhood updates result.
  Verify: Test multiple 里, verify correct school shows with contact info.

- [ ] **7. Add CSS styling**
  Spec ref: `spec.md > UI Layer`
  What to build: Add clean, readable CSS: centered container, readable font sizes, clear result display, proper spacing, Google-style search box styling.
  Acceptance: Page looks presentable. School name is prominent. Readable on both desktop and mobile.
  Verify: Open in browser, visually confirm styling is acceptable.

- [ ] **8. Final testing and verification**
  Spec ref: `prd.md > What We're Building`
  What to build: Test the complete flow: search for village → select from autocomplete → see school. Test edge cases: 共同學區, partial assignment 里.
  Acceptance: All user stories from PRD work correctly. No JavaScript errors in console.
  Verify: Walk through the user flow and confirm all acceptance criteria pass.

- [ ] **9. Submit to Devpost**
  Spec ref: `prd.md > What We're Building`
  What to build: Create Devpost submission: project name "新竹里別查學區", tagline about helping parents find school zones. Write description using scope/prd. Add screenshots. Upload docs artifacts.
  Acceptance: Submission is live on Devpost with all required fields.
  Verify: Open Devpost page, confirm submission shows green "Submitted" badge.
