from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestShoppingCart:
    def test_swa_12_add_remove_items_and_continue_shopping(self, driver):
        """SWA-12: Add items, remove items, and continue shopping"""
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        # Verify cart badge is empty initially
        assert inventory_page.get_cart_badge_count() == "0"

        # Add 3 items per SWA-12
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
        ]
        for item in items_to_add:
            inventory_page.add_item_to_cart(item)

        assert inventory_page.get_cart_badge_count() == "3"

        # Go to cart & remove 2 items
        inventory_page.go_to_cart()
        assert "cart.html" in driver.current_url
        assert len(cart_page.get_cart_item_names()) == 3

        cart_page.remove_item("Sauce Labs Bike Light")
        cart_page.remove_item("Sauce Labs Bolt T-Shirt")
        assert inventory_page.get_cart_badge_count() == "1"

        # Continue shopping & verify state on inventory page
        cart_page.continue_shopping()
        assert "inventory.html" in driver.current_url
        assert inventory_page.get_cart_badge_count() == "1"
        assert inventory_page.is_remove_button_displayed("Sauce Labs Backpack")