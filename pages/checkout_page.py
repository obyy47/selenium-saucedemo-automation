from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BTN = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BTN = (By.ID, "back-to-products")

    def fill_information(self, first_name, last_name, postal_code):
        if first_name:
            self.type_text(self.FIRST_NAME_INPUT, first_name)
        if last_name:
            self.type_text(self.LAST_NAME_INPUT, last_name)
        if postal_code:
            self.type_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BTN)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_total_price_text(self):
        return self.get_text(self.SUMMARY_TOTAL)

    def finish_checkout(self):
        self.click(self.FINISH_BTN)

    def get_complete_message(self):
        return self.get_text(self.COMPLETE_HEADER)

    def back_to_home(self):
        self.click(self.BACK_HOME_BTN)