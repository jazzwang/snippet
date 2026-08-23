import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # Connect to the running Edge instance using the debugging port
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        
        # Access the already open page or create a new one in the current context
        context = browser.contexts[0]
        page = await context.new_page()
        
        # Run your automation steps
        await page.goto("https://microsoft.com")
        print(f"Successfully connected! Page title is: '{await page.title()}'")
        
        # Optional: Keep the browser window open by not closing the connection immediately
        # await browser.close()

asyncio.run(main())
