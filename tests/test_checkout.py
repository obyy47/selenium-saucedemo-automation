import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestCheckout:
    @pytest.fixture
    def setup_checkout_page(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        login_page.load()
        login_page.login("standard_user", "secret_sauce")
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.go_to_cart()
        cart_page.proceed_to_checkout()
        return CheckoutPage(driver)

    def test_swa_41_all_information_fields_empty(self, setup_checkout_page):
        """SWA-41: All information fields empty shows an error"""
        checkout_page = setup_checkout_page
        checkout_page.fill_information("", "", "")

        assert "Error: First Name is required" in checkout_page.get_error_message()

    def test_swa_38_empty_first_name_shows_error(self, setup_checkout_page):
        """SWA-38: Empty First Name shows an error"""
        checkout_page = setup_checkout_page
        checkout_page.fill_information("", "obbyy", "12341234")

        assert "Error: First Name is required" in checkout_page.get_error_message()

    def test_swa_17_complete_checkout_with_valid_info(self, driver, setup_checkout_page):
        """SWA-17: Complete checkout with valid information"""
        checkout_page = setup_checkout_page
        inventory_page = InventoryPage(driver)

        checkout_page.fill_information("Robby", "Adriansyah", "1234")
        assert "checkout-step-two.html" in driver.current_url

        checkout_page.finish_checkout()
        assert "checkout-complete.html" in driver.current_url
        assert "Thank you for your order!" in checkout_page.get_complete_message()

        checkout_page.back_to_home()
        assert "inventory.html" in driver.current_url
        assert inventory_page.get_cart_badge_count() == "0"