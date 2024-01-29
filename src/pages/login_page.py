from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from src.pages.base_page import BasePage


class LoginPageLocators:
    LOCATOR_CUSTOMER_BUTTON = (
        By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[1]/button"
    )


class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        self.url = self.BASE_URL + 'login'
        super().__init__(*args, **kwargs)

    def go_to_page(self):
        self.goto(self.url)

    def make_search(self):
        by, value = LoginPageLocators.LOCATOR_CUSTOMER_BUTTON

        self.wait.until(ec.presence_of_element_located((by, value)))
        self.driver.find_element(by, value).click()
        self.wait.until(ec.url_contains('customer'))

        assert self.driver.current_url == self.BASE_URL + 'customer'
