from playwright.sync_api import Page, expect
# "From Playwright's synchronous API, give me the sync_playwright, Page, expect functionality."
# import playwright package, then import sync or async package and then fixture (Page) class

def test_verifyloginPage(page:Page): #page fixture is part of Page class
    page.goto("https://testautomationpractice.blogspot.com/") #.goto("") is used to pass URL
    myURL=page.url #capture the URL, predefined property hence no page.url()
    # IMP-A property represents information that an object already has, hence no need for ()
    print('URL of the page: ', myURL)
    expect(page).to_have_url("https://testautomationpractice.blogspot.com/") #expect() is used for assertion, used to verify the URL

def test_verifyTitle(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    myTitle=page.title() #capture page title, predefined method hence page.title()
    # IMP-A method represents an action/function that needs to be executed.
    print('Page title: ',myTitle)
    expect(page).to_have_title('Automation Testing Practice')
