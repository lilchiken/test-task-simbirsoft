from typing import TYPE_CHECKING

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

from src.pages.base_page import BasePage

if TYPE_CHECKING:
    from selenium.webdriver import Remote
    from selenium.webdriver.support.wait import WebDriverWait


class CustomerPageLocators:
    LOCATOR_CUSTOMER_SELECT = (
        By.XPATH, """//*[@id="userSelect"]"""
    )
    CUSTOMER_SELECT_VALUE = 'Harry Potter'
    LOCATOR_LOGIN_BUTTON = (
        By.XPATH, "/html/body/div/div/div[2]/div/form/button"
    )


class CustomerPage(BasePage):
    def __init__(self, *args, **kwargs):
        self.url = self.BASE_URL + 'customer'
        super().__init__(*args, **kwargs)

    def go_to_page(self):
        self.goto(self.url)

    @staticmethod
    def login(driver: 'Remote', wait: 'WebDriverWait'):
        by, value = CustomerPageLocators.LOCATOR_CUSTOMER_SELECT

        wait.until(ec.presence_of_element_located((by, value)))

        select = Select(driver.find_element(by, value))
        select_value = CustomerPageLocators.CUSTOMER_SELECT_VALUE
        select.select_by_visible_text(select_value)

        by, value = CustomerPageLocators.LOCATOR_LOGIN_BUTTON
        driver.find_element(by, value).click()
        wait.until(ec.url_contains('account'))

    def make_search(self):
        self.login(self.driver, self.wait)

        assert self.driver.current_url == self.BASE_URL + 'account'
