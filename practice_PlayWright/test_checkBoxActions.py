from playwright.sync_api import Page, expect

def test_verify_checkbox(page:Page):

    # Select any single checkbox
    page.goto('https://testautomationpractice.blogspot.com/')
    # page.get_by_label('Sunday').check()
    # page.wait_for_timeout(5000)

    # Perform action on multiple checkbox using list
    days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'] # list of labels of the checkboxes

    checkbox=[page.get_by_label(day) for day in days]  # checkbox contains list of elements(checkboxes)
    # days - contains labels of the elements
    # day - variable that stores the list of labels
    # page.get_by_label(day) - gets the elements (locator)
    # checkbox - variable that contains list of elements (locator)

    for action_checkbox in checkbox: # check all the checkboxes, perform action on individual checkbox in the list
        action_checkbox.check() #action_checkbox is the variable for elements in checkbox variable
        expect(action_checkbox).to_be_checked() # assertion
    page.wait_for_timeout(3000)

    # Uncheck last three
    for action_checkbox in checkbox[-3:]: # use slicing to select range
        action_checkbox.uncheck() # uncheck() uncheck already selected checkbox
    page.wait_for_timeout(3000)

    # Toggle checkboxes
    for action_checkbox in checkbox:
        if action_checkbox.is_checked():
            action_checkbox.uncheck()
        else:
            action_checkbox.check()
    page.wait_for_timeout(5000)





