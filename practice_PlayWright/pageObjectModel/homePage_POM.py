from playwright.sync_api import Playwright, Page

class HomePage:
    # LOCATORS
    def __init__(self,page:Page):
        self.page=page
        self.product_list_locator="div#tbodyid div.card h4.card-title a"
        self.add_to_cart_button=self.page.locator('a:has-text("Add to cart")')
        self.cart_link=self.page.locator('#cartur')

    # ACTION METHOD
    def add_product_to_cart(self,product_name): # product_name is a parameter called from the test case
        products=self.page.locator(self.product_list_locator)
        count=products.count()

        for i in range(count):
            name=products.nth(i).text_content().strip()
            if name==product_name:
                products.nth(i).click()
                break

        # HANDLE DIALOG
        self.page.on("dialog", lambda dialog:dialog.accept())
        self.add_to_cart_button.click()

    def goto_cart(self):
        self.cart_link.click()




