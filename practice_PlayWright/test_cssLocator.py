# tag#id
# tag.class
# tag[attribute=value]
# tag.class[attribute=value]

# tag is optional

from playwright.sync_api import Page, expect

# def test_verify_css_locator(page:Page):
#     page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
#     page.wait_for_timeout(5000)
#     page.get_by_placeholder('Username').fill('Admin')
#     page.wait_for_timeout(3000)
#     page.locator('input.oxd-input.oxd-input--active').fill('admin123') #check class properly add . if there are any spaces
#     # initial class "oxd-input oxd-input--active", either give . or use only first statement oxd-input
#     page.wait_for_timeout(3000)
#     page.locator('button.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button').click()
#     # initial class "oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"
#     page.wait_for_timeout(5000)

def test_verify_css_locators(page:Page):
    page.goto('https://demowebshop.tricentis.com/')

    # 1. tag#id
    # page.locator('input#small-searchterms').fill('shirt')
    # page.wait_for_timeout(5000)

    # 2. tag.class
    # page.locator('.search-box-text.ui-autocomplete-input').fill('shirt')
    # page.wait_for_timeout(5000)
    #
    # 3. tag[attribute=value]
    # page.locator("input[name=q]").fill('shirt')
    # page.wait_for_timeout(5000)
    #
    # 4. tag.class[attribute=value]
    page.locator('input.search-box-text.ui-autocomplete-input[name=q]').fill('shirt')
    # no "" inside "", but we can use '' inside ""
