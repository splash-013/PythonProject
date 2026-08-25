from playwright.sync_api import Playwright, expect
import time
import datetime

def test_screenshots(playwright:Playwright):
    browser=playwright.firefox.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.goto('https://demowebshop.tricentis.com/')

    #timestamp
    #timestamp=str(int(time.time())) # .time() function is in float/int format, we need to type cast and convert it into String

    #timestamp - date and time
    timestamp=datetime.datetime.now().strftime('%Y%m%d_%H%M%S')  # give the screenshot a unique filename based on the current date/time.

    # partial page screenshot and add a timestamp in the screenshot
    page.screenshot(path=f'screenshots/homepage_{timestamp}.png') # provide path of the folder and give the file name

    # full page screenshot
    page.screenshot(path=f'screenshots/homepage_{timestamp}.png', full_page=True)

    # specific element
    logo=page.get_by_alt_text('Tricentis Demo Web Shop')
    logo.screenshot(path=f'screenshots/logo_{timestamp}.png')

    # specific section
    section=page.locator('.product-grid.home-page-product-grid')
    section.screenshot(path=f'screenshots/section_{timestamp}.png')