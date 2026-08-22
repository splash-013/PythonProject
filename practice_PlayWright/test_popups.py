import pytest
from playwright.sync_api import expect, Playwright

# IMPORTANT

def test_popups(playwright:Playwright):
    browser=playwright.firefox.launch(headless=False)
    browser_context=browser.new_context()
    browser_page=browser_context.new_page()

    browser_page.goto('https://testautomationpractice.blogspot.com/')

    # function should be created before taking any action on the element
    x=lambda popup:popup.wait_for_load_state()
    browser_page.on('popup',x)

    i=browser_page.locator('#PopUp')
    i.scroll_into_view_if_needed()
    i.click()

    browser_page.wait_for_timeout(5000)

    # Check all the popup pages
    all_popups=browser_context.pages # .pages is the predefined function, These are playwright pages
    print("Total popups available: ",len(all_popups))

    # Get all the popup URL
    for p in all_popups: # pop up playwright pages variable
        print('URL:',p.url) # .url is the pred defined function

        # Perform an action on an element in one of the popup page
        if "https://playwright.dev/" in p.url: # condition to select the specific popup to perform an action, we can get the title as well
            p.locator('.getStarted_Sjon').click()
            p.wait_for_timeout(5000)


