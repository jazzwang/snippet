# Development Notes

## 2024-07-25

- 需求：為了一些自動化的需求，需要在 Island Browser 裡面透過 Chrome DevTool 開啟多個內網 URL
- 參考：How to Open URL in New Tab using JavaScript?
  - https://www.geeksforgeeks.org/how-to-open-url-in-new-tab-using-javascript/
- 解法：
  ```js
  window.open(URL, '_blank');
  ```
