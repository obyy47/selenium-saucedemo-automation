from pages.login_page import LoginPage


class TestLogin:
    def test_swa_1_login_standard_user(self, driver):
        """SWA-1: Log in with standard_user"""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        assert "inventory.html" in driver.current_url

    def test_swa_2_login_locked_out_user(self, driver):
        """SWA-2: Log in with locked_out_user shows error message"""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("locked_out_user", "secret_sauce")

        assert "Sorry, this user has been locked out" in login_page.get_error_message()

    def test_swa_28_valid_username_incorrect_password(self, driver):
        """SWA-28: Valid username with incorrect password shows error"""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "wrongpass123")

        assert (
            "Epic sadface: Username and password do not match any user in this service"
            in login_page.get_error_message()
        )

    def test_swa_33_empty_username_and_empty_password(self, driver):
        """SWA-33: Empty username and empty password shows error"""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("", "")

        assert "Epic sadface: Username is required" in login_page.get_error_message()