const puppeteer = require('puppeteer');

(async() => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');
  const session = await page.target().createCDPSession();
  await session.send('Page.enable');
  const {data} = await session.send('Page.captureSnapshot');
  console.log(data);
  await browser.close();
})();