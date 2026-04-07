# Hsinchu School Zone Lookup — Technical Spec

## Stack
- **Language**: HTML5 + Vanilla JavaScript (ES6+)
- **Styling**: CSS3 (embedded in HTML)
- **Libraries**: None required — pure vanilla JS for simplicity
- **Data**: Embedded JSON in `<script>` tag

## Runtime & Deployment
- **Target**: Single HTML file, opens directly in browser (file:// protocol)
- **Environment**: Any modern browser (Chrome, Firefox, Safari, Edge)
- **No server required** — runs entirely client-side

## Architecture Overview
```
┌─────────────────────────────────────┐
│           index.html                │
├─────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  │
│  │  UI Layer   │  │  Data Layer  │  │
│  │ (search)    │  │ (school data)│  │
│  └──────┬──────┘  └──────┬──────┘  │
│         │                │          │
│         ▼                ▼          │
│  ┌─────────────────────────────────┐│
│  │      Logic Layer                 ││
│  │  (autocomplete, lookup)          ││
│  └─────────────────────────────────┘│
└─────────────────────────────────────┘
```

## Components

### UI Layer
- **Header**: Title "新竹里別查學區"
- **Search Box**: Google-style input with placeholder "搜尋新竹市里名稱..."
- **Autocomplete Dropdown**: Shows matching 里 with district tags
- **Neighborhood Selector**: `<select id="neighborhood">` — shown only when needed
- **Result Display**: Shows assigned school(s) with contact info

### Logic Layer
- **Autocomplete**: Filter villages as user types, show top 20 matches
- **School Lookup**: Find assigned school(s) based on village + optional neighborhood
- **Event Listeners**: Input events for search, change events for selects

### Data Layer
- **Embedded JSON**: 114 Academic Year school zone data structure
- **Data Format**:
```javascript
const schoolData = {
  "東區": {
    "高峰里": { schools: ["建華國中"] },
    "仙宮里": { schools: ["建華國中"] },
    // ...
  },
  // ...
};
```

## Data Model

### schoolZoneData
```javascript
{
  [districtName: string]: {
    [villageName: string]: {
      schools: string[],           // for entire village
      neighborhoods?: {            // for partial assignments
        [neighborhoodRange: string]: {
          schools: string[]
        }
      }
    }
  }
}
```

### UI State
```javascript
{
  selectedVillage: { name: string, district: string } | null,
  selectedNeighborhood: string | null
}
```

## File Structure
```
devpost/
├── index.html          # Single file containing HTML, CSS, JS, and data
├── docs/
│   ├── learner-profile.md
│   ├── scope.md
│   ├── prd.md
│   ├── spec.md
│   ├── checklist.md
│   └── reflection.md
└── process-notes.md
```

## Key Technical Decisions

### 1. Embedded JSON vs. External Data
- **Decision**: Embed data directly in HTML as JavaScript object
- **Why**: Avoids CORS issues, works offline, single file
- **Tradeoff**: File size larger, data updates require editing HTML

### 2. Google-Style Search vs. Dropdowns
- **Decision**: Single search box with autocomplete instead of district → village dropdowns
- **Why**: The PDF's school zones don't align perfectly with administrative districts (東區/北區/香山區). A unified search is less confusing and more user-friendly.
- **Tradeoff**: Slightly more complex JS, but better UX

### 3. School Display Format
- **Decision**: Display all schools if multiple (共同學區), separated by "、" with contact info below
- **Why**: Parents need to know all options, some 里 have 2-3 school choices
- **Tradeoff**: Need clear visual separation

## Dependencies & External Services
- None — fully self-contained
- No CDN needed (no external libraries)

## Open Issues
- Need to verify all 里 data is complete and accurate
- School contact info uses placeholder data (need to verify with official source)

## Implementation Priority
1. Create HTML skeleton with search UI
2. Embed school zone data (most time-consuming step)
3. Implement autocomplete logic
4. Implement school lookup function
5. Add CSS styling
6. Test with sample 里 names
