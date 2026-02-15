# AGENT GUIDELINES

This document provides guidelines for AI agents operating within this repository. Adhering to these guidelines ensures consistency, maintainability, and high code quality across diverse projects.

## 1. Build, Lint, and Test Commands

This repository contains projects in multiple languages. Always infer the correct commands by examining relevant project configuration files within the specific sub-project directory.

### General Principles:
*   **Always Verify**: Before making changes, always check for existing tests and run them to ensure a safety net.
*   **Post-Change Verification**: After making changes, run relevant linting, type-checking, and test commands to verify correctness and adherence to standards.
*   **Single Test Execution**: Prioritize running individual tests when possible to speed up feedback loops.

### Language-Specific Guidance:

#### JavaScript/TypeScript (Node.js/React projects)
*   **Configuration Files**: Look for `package.json` for scripts (e.g., `npm run build`, `npm test`, `npm run lint`).
*   **Install Dependencies**: `npm install` or `yarn install`
*   **Build**: `npm run build` or `yarn build` (check `package.json` `scripts` section)
*   **Lint**: `npm run lint` or `yarn lint` (check `package.json` `scripts` section). If no explicit lint script, infer from common tools like ESLint (e.g., `npx eslint .`).
*   **Test**: `npm test` or `yarn test`.
    *   **Single Test**: Look for patterns in `package.json` scripts. Common approaches include `npm test -- <path/to/test.js>` or environment variables (e.g., `TEST_FILE=<path> npm test`). If not found, `jest <path/to/test.js>` or `npx mocha <path/to/test.js>` might work depending on the test runner.

#### Java (Gradle projects)
*   **Configuration Files**: `build.gradle`
*   **Build**: `./gradlew build`
*   **Lint/Check**: `./gradlew check` (often includes linting, tests, and other checks)
*   **Test**: `./gradlew test`
    *   **Single Test**: `./gradlew test --tests "com.example.package.MyTestClass.testMethodName"` or `./gradlew test --tests "*MyTestClass*"`

#### Python (pip/poetry projects)
*   **Configuration Files**: `requirements.txt`, `pyproject.toml` (for Poetry or PDM)
*   **Install Dependencies**: `pip install -r requirements.txt` or `poetry install`
*   **Lint**: `ruff check .`, `flake8 .`
*   **Test**: `pytest`
    *   **Single Test**: `pytest <path/to/test_file.py>::test_function_name` or `pytest <path/to/test_file.py>`

### Shell Scripting / Makefiles
*   **Configuration Files**: `Makefile`
*   **Execution**: `make <target>` (e.g., `make build`, `make test`). Examine the `Makefile` for available targets.

## 2. Code Style Guidelines

When modifying existing code or adding new features, **always prioritize adhering to the existing conventions of the specific sub-project you are working in.** If no explicit rules are found, follow these general best practices:

### Imports:
*   **Consistency**: Maintain consistent import ordering and grouping.
*   **Clarity**: Avoid wildcard imports (`from module import *`). Explicitly import what is needed.
*   **Grouping**: Group imports by standard library, third-party, and local modules, with a blank line between groups.

### Formatting:
*   **Indentation**: Use spaces, not tabs. Follow the existing indentation level (2 or 4 spaces).
*   **Line Length**: Aim for a maximum of 120 characters per line.
*   **Whitespace**: Use consistent whitespace around operators, function arguments, and control structures.
*   **Braces**: Follow existing brace style (e.g., K&R, Allman).

### Types:
*   **Type Hinting (Python/TypeScript/Java)**: Use type hints/annotations where appropriate to improve code readability and maintainability.
*   **Readability**: Do not over-complicate types. Prefer clear and concise types.

### Naming Conventions:
*   **Descriptive**: Use clear and descriptive names for variables, functions, classes, and files.
*   **Case Sensitivity**:
    *   **Python**: `snake_case` for variables and functions, `PascalCase` for classes.
    *   **JavaScript/TypeScript**: `camelCase` for variables and functions, `PascalCase` for classes.
    *   **Java**: `camelCase` for variables and methods, `PascalCase` for classes, `SCREAMING_SNAKE_CASE` for constants.
*   **File Names**: Use `kebab-case` or `snake_case` for filenames, depending on the project's existing convention.

### Error Handling:
*   **Graceful Degradation**: Handle errors gracefully to prevent application crashes.
*   **Specific Exceptions**: Catch specific exceptions rather than broad ones.
*   **Logging**: Use appropriate logging levels (debug, info, warn, error) for different types of events.
*   **User Feedback**: Provide meaningful error messages to users when applicable.

## 3. Cursor/Copilot Rules

No explicit Cursor rules (`.cursor/rules/`, `.cursorrules`) or Copilot rules (`.github/copilot-instructions.md`) were found in this repository. Therefore, rely on the general guidelines above and the existing code patterns to infer best practices.