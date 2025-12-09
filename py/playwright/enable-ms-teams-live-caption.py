import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.get_by_role("button", name="More", exact=True).click()
    page.get_by_text("Language and speech").click()
    page.get_by_role("menuitemcheckbox", name="Show live captions").click()
    page.get_by_role("button", name="More", exact=True).click()
    page.get_by_text("Settings", exact=True).click()
    page.get_by_text("Mute notifications").click()
    page.get_by_test_id("hamburger-button").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
