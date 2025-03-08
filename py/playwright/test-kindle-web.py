import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=1209600&openid.return_to=https%3A%2F%2Fread.amazon.com%2F%3Fasin%3DB0DM6BHQYR&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_kindle_mykindle_us&openid.mode=checkid_setup&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    page.get_by_role("textbox", name="Email or mobile phone number").click()
    page.get_by_role("textbox", name="Email or mobile phone number").fill("jazz.wang@example.com")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("textbox", name="Password").fill("THIS-IS-MY-PASSWORD")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("button", name="Next page").click()
    page.get_by_role("button", name="Next page").click()
    page.get_by_role("button", name="Next page").click()
    page.get_by_role("button", name="Next page").click()
    page.get_by_role("button", name="Next page").click()
    page.get_by_role("button", name="Next page").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

