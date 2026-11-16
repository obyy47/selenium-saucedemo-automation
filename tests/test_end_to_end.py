from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestEndToEnd:
    def test_swa_27_complete_user_journey_standard_user(self, driver):
        """SWA-27: Complete user journey with standard_user"""
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        # 1. Login
        login_page.load()
        login_page.login("standard_user", "secret_sauce")
        assert "inventory.html" in driver.current_url

        # 2. Add 2 items
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.add_item_to_cart("Sauce Labs Bike Light")
        assert inventory_page.get_cart_badge_count() == "2"

        # 3. Cart -> Checkout
        inventory_page.go_to_cart()
        cart_page.proceed_to_checkout()

        # 4. Fill customer info & verify total ($43.18)
        checkout_page.fill_information("Robby", "Adriansyah Fadillah", "40227")
        assert "checkout-step-two.html" in driver.current_url
        assert "$43.18" in checkout_page.get_total_price_text()

        # 5. Finish order & Back Home
        checkout_page.finish_checkout()
        assert "Thank you for your order!" in checkout_page.get_complete_message()

        checkout_page.back_to_home()
        assert "inventory.html" in driver.current_url
        assert inventory_page.get_cart_badge_count() == "0"

        # 6. Logout
        inventory_page.logout()
        assert driver.current_url == LoginPage.URL