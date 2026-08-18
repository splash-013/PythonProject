import pytest
from playwright.sync_api import Page, expect


@pytest.mark.skip
def test_dialog(page:Page):

    # Approach 1
    def handle_dialog(dialog):  # user defined function
        dialog.accept()

    page.on('dialog',handle_dialog())

    page.goto('https://testautomationpractice.blogspot.com/')
    simpleAlert=page.locator('#alertBtn')
    simpleAlert.scroll_into_view_if_needed()
    page.wait_for_timeout(3000)
    simpleAlert.click()
    page.wait_for_timeout(5000)

# Approach 2
    @pytest.mark.skip
    def test_dialog(page: Page):

        x=lambda dialog:dialog.accept()  # function to Accept/OK the dialog box
        page.on("dialog",x)

    page.goto('https://testautomationpractice.blogspot.com/')
    simpleAlert = page.locator('#alertBtn')
    simpleAlert.scroll_into_view_if_needed()
    page.wait_for_timeout(3000)
    simpleAlert.click()
    page.wait_for_timeout(5000)

# Example 3
# Alert - Ok or Cancel

def test_confirmation_dialog(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    # Function to accept/OK
    # x=lambda con_dialog:con_dialog.accept()
    # page.on("dialog",x)

    # Function to Cancel
    x=lambda con_dialog:con_dialog.dismiss()
    page.on('dialog',x)

    confDialog=page.locator('#confirmBtn')
    confDialog.scroll_into_view_if_needed()
    page.wait_for_timeout(3000)
    confDialog.click()
    text=page.locator('#demo').inner_text() # .inner_text() get the visible text content from a web element
    print("Output text :",text) # get text after Ok or Cancel function is called
    page.wait_for_timeout(5000)








