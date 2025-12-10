import re, os
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    ## force to use 'Chrome - Mac' user_agent string
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"

    if os.path.exists('sso-storage.json'):
      print("[INFO] sso-storage.json found. loading into browser context.")
      context = browser.new_context(storage_state='sso-storage.json', user_agent=user_agent)
    else:
      context = browser.new_context(user_agent=user_agent)
    
    page = context.new_page()
    page.goto("https://myapps.microsoft.com/")
    input("Press Enter to close the browser...")
    context.storage_state(path="sso-storage.json")
    
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
