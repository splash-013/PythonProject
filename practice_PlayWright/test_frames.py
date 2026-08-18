# Frames are web pages or group of elements embedded in another web page
# A frame (iframe) is a separate HTML page embedded inside another HTML page.
# page.frames() is used to know how many frames exist on the web page
# page.frame_locator() is used to the get the frame present on web page
# Steps - 1.Get the frame using .frame or .frame_locator  2.Now located the element in that frame
#page.frame() → gets ONE specific frame
#page.frames → gets ALL frames on the page

import pytest
from playwright.sync_api import Page, expect

def test_frames(page:Page):
    page.goto('https://ui.vision/demo/webtest/frames/')

    # get number of frames
    x=page.frames # frames is a list
    print('Total no of frames:',len(x)) # hence len() is used to get the total no of frames list

    # FRAME 1
    # frame1=page.frame_locator("frame[src='frame_1.html']") # get the frame using CSS

    # frame1=page.frame(name=" add name of the frame if present") # get the frame using frame name

    frame1=page.frame(url='https://ui.vision/demo/webtest/frames/frame_1') # get the frame using URL

    input1=frame1.locator("input[name='mytext1']") # do not use page. use the frame page name
    input1.fill("Hello World!!")

    expect(input1).to_have_value("Hello World!!")

    page.wait_for_timeout(5000)


