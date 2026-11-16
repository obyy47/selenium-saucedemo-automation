from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    BURGER_MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def _product_slug(self, product_name):
        return product_name.lower().replace(" ", "-")

    def add_item_to_cart(self, product_name):
        locator = (By.ID, f"add-to-cart-{self._product_slug(product_name)}")
        self.click(locator)

    def is_remove_button_displayed(self, product_name):
        locator = (By.ID, f"remove-{self._product_slug(product_name)}")
        return self.is_element_present(locator)

    def get_cart_badge_count(self):
        if self.is_element_present(self.CART_BADGE):
            return self.get_text(self.CART_BADGE)
        return "0"

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def logout(self):
        self.click(self.BURGER_MENU_BTN)
        self.click(self.LOGOUT_LINK)