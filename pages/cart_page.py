from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "inventory_item_name")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")
    CHECKOUT_BTN = (By.ID, "checkout")

    def get_cart_item_names(self):
        elements = self.driver.find_elements(*self.CART_ITEMS)
        return [el.text for el in elements]

    def remove_item(self, product_name):
        slug = product_name.lower().replace(" ", "-")
        self.click((By.ID, f"remove-{slug}"))

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BTN)

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BTN)