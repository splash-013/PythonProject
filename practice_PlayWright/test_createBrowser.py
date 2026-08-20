import pytest_ordering
from playwright.sync_api import Page, expect, Playwright

# BROWSER > CONTEXT > PAGES
def test_create_browser(playwright:Playwright):

    # CREATE A BROWSER
    # Approach 1
    # chrome=playwright.chromium
    # browser=chrome.launch()

    # Approach 2
    # default headless=True
    browser=playwright.chromium.launch(headless=False)

    #CREATE BROWSER CONTEXT
    context1=browser.new_context()
    context2=browser.new_context()

    #CREATE PAGE
    page1=context1.new_page()
    page2=context1.new_page()

    page1.goto('https://playwright.dev/python/')
    page1.wait_for_timeout(3000)
    expect(page1).to_have_title('Fast and reliable end-to-end testing for modern web apps | Playwright Python')

    page2.goto('https://www.selenium.dev/')
    page2.wait_for_timeout(3000)
    expect(page2).to_have_title('Selenium')


