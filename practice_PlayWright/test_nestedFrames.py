import pytest
from playwright.sync_api import Page, expect


# Fixture for common page navigation
@pytest.fixture()
def main_page(page:Page):
    page.goto('https://ui.vision/demo/webtest/frames/')
    return page

@pytest.mark.skip
def test_frame1(main_page:Page):
    #page.goto('https://ui.vision/demo/webtest/frames/')
    #frame1=page.frame_locator("frame[src='frame_1.html']")
    frame1=main_page.frame(url='https://ui.vision/demo/webtest/frames/frame_1')
    element1=frame1.locator("input[name='mytext1']")
    element1.fill("Hello World!!")
    frame1.wait_for_timeout(5000)

@pytest.mark.skip
def test_frame2(main_page:Page):
    #page.goto('https://ui.vision/demo/webtest/frames/')
    frame2=main_page.frame(url='https://ui.vision/demo/webtest/frames/frame_2')
    element2=frame2.locator("input[name='mytext2']")
    element2.fill('Hello World 2!!')
    frame2.wait_for_timeout(5000)

def test_frame3(main_page:Page):
    #page.goto('https://ui.vision/demo/webtest/frames/')
    frame3=main_page.frame(url='https://ui.vision/demo/webtest/frames/frame_3')
    element3=frame3.locator("input[name='mytext3']")
    element3.fill("Hello World 3!!")

    #get total no of child frames
    child_frame=frame3.child_frames
    print("Total no on child frames in frame 3: ",len(child_frame))

    inner_frame=child_frame[0]
    radiobutton=inner_frame.get_by_label("I am a human")
    radiobutton.scroll_into_view_if_needed()
    radiobutton.click()
    frame3.wait_for_timeout(5000)
