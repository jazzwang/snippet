# How to install Chrome Extension into Playwright managed Chromium Browser

- 需求：
  - 因為 Edge Device Management Policy, 一些自動化測試需要改 user-agent 才有辦法正確完成身份認證。（還沒考慮 MFA，光在 Windows 系統上，如果 user-agent 不正確就沒辦法登入）

## 2025-11-26

- https://playwright.dev/python/docs/chrome-extensions

## 2025-11-28

- Playwright: Loading Chrome Extensions
  - https://owlfeatherworkshop.ca/tech/playwright-chrome-extensions/
- 2025-09-26
  - How to use Headless Chrome Extensions for Web Scraping
  - https://scrapfly.io/blog/posts/how-to-use-browser-extensions-with-playwright-puppeteer-and-selenium#headless-browser-extensions-summary
  - 這篇文章介紹了怎麼用 Selenium, Playwright 甚至 Puppeteer 安裝 Chrome Extension
