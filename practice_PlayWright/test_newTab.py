from playwright.sync_api import Playwright, expect

def test_newtab(playwright:Playwright):
    browser=playwright.firefox.launch(headless=False)
    context=browser.new_context()
    parentPage=context.new_page()

    parentPage.goto('https://testautomationpractice.blogspot.com/')

    # Handle the event, new tab

    with parentPage.expect_popup() as popup_info: # I am expecting a new tab/popup. When it happens, keep information about it in popup_info
        tab_button=parentPage.get_by_role("button", name="New Tab")
        tab_button.scroll_into_view_if_needed()
        tab_button.click()

        newtab=popup_info.value # Give me the actual popup/new-tab object that was captured.
        # now to interact with the elements on new tab page, newtab variable is used


        parentPage.wait_for_timeout(5000)