# Chrome DevTools for Agents
## Introduction
### What it is
* New UI surface for DevTools
* Enables closed feedback loop for coding agents
* Announced September last year (relative to talk)
* Solves agent debugging dead ends (e.g., `APP_ERR_1003`)
### Speaker's Background
* Matthias Rohmer
* Learned web development in 2014 with DevTools
* Believes agents are "missing out" without DevTools
### Agent Benefit
* Access to runtime data (e.g., network responses)
* Guides agent to right file via source maps
* Example prompt: "Go to localhost, signup, debug and fix the error when signing up with test and 1234."
## Foundational Technologies
### Core Components
* NPM package
* MCP server
* CLI
* Skills
### Underlying Libraries
* Chrome for testing
* Puppeteer
### Skills
* Total of six skills initially
* Two categories:
    * Troubleshooting and general usage (Chrome DevTools and Chrome DevTools CLI skills)
    * Expert knowledge (Accessibility debugging, Memory leak debugging, Optimized LCP)
* Skill set to expand with modern web guidance
## Capabilities & Use Cases
### Tools Categories
* Input automation
* Network automation
* Navigation automation
* Emulation tools
* Debugging tools (e.g., screenshots)
* Performance tools (e.g., traces, Lighthouse audits)
### Example 1: Fixing Complex UI Flows
* **Prompt:** "Go to localhost, debug and fix the error when signing up with test and 1234."
* **Actions:** Navigate, fill form, capture Console logs/network requests, combine pointers, fix code, validate fix.
* **Tools used:** Input automation, network, navigation automation.
* **Partner case study:** CyberAgent audited 230 Storybook stories across 32 components in 1 hour.
### Example 2: One-off Bug Validation
* **Prompt:** "go to developer.chrome.com. Check the same navigation items are visible on desktop, tablet, and mobile viewports."
* **Actions:** Open Chrome, resize viewport (desktop, tablet, mobile), take screenshots, interact with burger menu, cross-check.
* **Tools used:** Emulation tools, debugging tools (screenshots).
* **Benefit:** Automates testing journey across viewports and nested menus.
### Example 3: Scaling Expertise
* **Problem:** Agent might burn token budget fixing random things with generic prompts.
* **Solution:** Specialized tools test for known problems.
* **Benefit:** Improve performance, accessibility, SEO in areas you're not inherently familiar with.
* **Performance Prompt:** "Go to localhost, run a performance trace, and act on all findings."
* **Tools used:** Performance traces, Lighthouse audits (accessibility, best practices, SEO, agentic browser agent's audit).
### Example 4: Persisting Actions to Scripts (CLI Focus)
* **Prompt:** "Persist your previous actions in DevTools to a well-named script file using the DevTools CLI."
* **Benefit:** Rerun actions outside of agent loop, create shell scripts (e.g., opening page, emulating viewports, taking screenshots).
* **Requirement:** Agent needs access to DevTools CLI and related skill.
## Security Considerations
### Default Behavior
* Uses a separate, anonymous browser profile by default.
* Does NOT have access to Chrome's password manager.
### autoConnect Warning
* Can connect to personal Chrome profile.
* Risk of unintended costs/consequences (e.g., ordering balloons).
* "Carefully decide what you give agents access to."
## Configuration
### Methods
* **MCP Server:** Modify `args` array in config file (e.g., `.gemini/settings.json`, `.mcp.json`).
* **CLI:** Explicitly include desired option in the prompt.
### Key Options
* **`channel`:** Specify Chrome channel (e.g., "Stable").
* **`experimentalScreencast`:** Enable experimental screencasts.
* **Turn off tool categories:** For MCP server to save tokens.
* **`autoConnect`:**
    * Allows connecting to an already running Chrome instance.
    * Requires enabling "Allow Remote Debugging for This Browser Instance" in Chrome's Inspect > Remote Debugging sidebar.
    * Shares "screen" with coding agent.
    * Potential security risks if connected to a personal profile.
## Getting Started
### Release Status
* First stable release, version 1.0 (or ~1.01).
### Resources
* **Install Instructions, Docs, Use Cases (including autoConnect):** developer.chrome.com
* **Video Tutorial (Setting up):** youtube.com/google/dtasetup (beginning of a series)
* **Open-Source Project:** GitHub (for contributions, feature discussions, issues)
### Engagement
* Reach out on social with use case ideas.
* Contribute to the project on GitHub.
