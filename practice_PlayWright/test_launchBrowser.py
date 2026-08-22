from playwright.sync_api import sync_playwright
# "From Playwright's synchronous API, give me the sync_playwright (start PW to use browser) functionality."
with sync_playwright() as p: #Start the Playwright system so that we can work with browsers, "Start/create the Playwright environment."

    browser=p.chromium.launch(headless=False) #launch the Chromium browser
    context=browser.new_context() #Create a new, isolated browser session
    page=context.new_page() #Create a new browser tab inside that session
    page.goto("https://testautomationpractice.blogspot.com/")




