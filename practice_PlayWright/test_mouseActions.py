import pytest
from playwright.sync_api import Page, expect

@pytest.mark.skip
def test_mousehover(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    page.locator('.dropbtn').hover() # mouse hover

    hover01=page.locator('.dropdown-content').nth(0)
    hover01.hover()
    # page.locator('.dropdown-content:nth-child(2)') # .nth child for parent and child

@pytest.mark.skip
# right click button
def test_mouserightclick(page:Page):
    page.goto('https://swisnl.github.io/jQuery-contextMenu/demo.html')
    rightButton=page.locator('.context-menu-one.btn.btn-neutral')
    rightButton.click(button='right')
     # hover01 = page.locator('.dropdown-content').nth(0)
    # hover01.hover()

@pytest.mark.skip
# double click
def test_doubleclick(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    #page.get_by_text('Copy Text').dblclick()
    button=page.locator("button[ondblclick='myFunction1()']")
    button.dblclick()
    field2=page.locator('#field2')
    expect(field2).to_have_value("Hello World!")

# drag and drop
def test_dragdrop(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    source=page.locator('#draggable')
    target=page.locator('#droppable')
    source.scroll_into_view_if_needed()  # page scroll to see the element
    page.wait_for_timeout(3000)

    # Approach 1
    # source.hover()
    # page.mouse.down() # perform action
    # target.hover()
    # page.mouse.up()

    # Approach 2  .drag_to()
    source.drag_to(target)










    page.wait_for_timeout(5000)