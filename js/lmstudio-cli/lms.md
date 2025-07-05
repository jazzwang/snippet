# LM Studio CLI

- Git Repo
  - https://github.com/lmstudio-ai/lms
- Website:
  - https://lms.dev/
- Document
  - https://lmstudio.ai/docs/cli

## 2025-07-05

- ( 2025-07-05 00:40:12 )
- 實測：
```
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 6.8.0-1027-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
Last login: Fri Jun 27 09:09:10 2025 from ::1
@jazzwang ➜ /workspaces/codespaces-blank (main) $ npx lmstudio install-cli
Need to install the following packages:
lmstudio@0.0.30
Ok to proceed? (y)



   ┌ Error ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
   │                                                                                                                                    │
   │   Cannot find LM Studio installation                                                                                               │
   │                                                                                                                                    │
   │   LM Studio CLI (lms) is shipped with the latest version of LM Studio. Please install LM Studio first. You can download it from:   │
   │                                                                                                                                    │
   │       https://lmstudio.ai/                                                                                                         │
   │                                                                                                                                    │
   │   If you have just installed LM Studio, please run it at least once before running this tool again.                                │
   │                                                                                                                                    │
   └────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

npm notice
npm notice New major version of npm available! 10.8.2 -> 11.4.2
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.4.2
npm notice To update run: npm install -g npm@11.4.2
npm notice
@jazzwang ➜ /workspaces/codespaces-blank (main) $
```

## 2026-07-06

- 看起來是要先裝 LM Studio 才有辦法用 CLI
- https://lmstudio.ai/docs/cli