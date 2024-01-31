from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from src.pages.base_page import BasePage


class LoginPageLocators:
    CUSTOMER_LOGIN_BUTTON = (
        By.CSS_SELECTOR, "button[ng-click*='customer']"
    )


class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        self.url = self.BASE_URL + 'login'
        super().__init__(*args, **kwargs)

    def go_to_page(self):
        self.goto(self.url)

    def redirect_to_customer_login(self):
        by, value = LoginPageLocators.CUSTOMER_LOGIN_BUTTON

        self.wait.until(ec.presence_of_element_located((by, value)))
        self.driver.find_element(by, value).click()
        self.wait.until(ec.url_contains('customer'))

        assert self.driver.current_url == self.BASE_URL + 'customer'
