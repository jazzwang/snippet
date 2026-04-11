# Join Teams Meeting Action

A GitHub Action that joins Microsoft Teams meetings using Playwright with cookie-based authentication.

## Usage

```yaml
on:
  workflow_dispatch:
    inputs:
      profile:
        description: 'Profile to use (profile1, profile2, profile3)'
        required: true
        type: choice
        options:
          - profile1
          - profile2
          - profile3

jobs:
  join-teams:
    runs-on: ubuntu-latest
    steps:
      - name: Join Teams Meeting
        uses: ./
        with:
          profile: ${{ github.event.inputs.profile }}
          meeting-url: ${{ secrets.TEAMS_MEETING_URL }}
        env:
          TEAMS_PROFILES: ${{ secrets.TEAMS_PROFILES }}
```

## Secrets

Configure the following secrets in your GitHub repository:

| Secret | Description |
|--------|-------------|
| `TEAMS_MEETING_URL` | Default Microsoft Teams meeting URL |
| `TEAMS_PROFILES` | JSON object containing profile cookies |

### TEAMS_PROFILES Format

```json
{
  "profile1": {
    "cookie1": "value1",
    "cookie2": "value2"
  },
  "profile2": {
    "cookie1": "valueA",
    "cookie2": "valueB"
  },
  "profile3": {
    "cookie1": "valueX",
    "cookie2": "valueY"
  }
}
```

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `profile` | Yes | Profile name to use (profile1, profile2, or profile3) |
| `meeting-url` | Yes | Microsoft Teams meeting URL |

## Outputs

Logs are uploaded as artifacts with 7-day retention.

## How It Works

1. Parses the `TEAMS_PROFILES` secret JSON to extract cookies for the selected profile
2. Builds a Docker image with Playwright and Chromium
3. Pushes the image to GitHub Container Registry (GHCR) as public
4. Runs a container with the meeting URL and cookies as environment variables
5. Playwright navigates to the Teams meeting URL with the provided cookies
6. Automatically clicks the join button
7. Uploads logs and screenshots as artifacts

## Sample Cookie获取

To get Teams cookies:
1. Open Microsoft Teams in Chrome/Edge
2. Open Developer Tools (F12)
3. Go to Application > Cookies > teams.microsoft.com
4. Copy cookie names and values

## License

MIT