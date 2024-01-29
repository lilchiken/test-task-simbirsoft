from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from src.pages.base_page import BasePage
from src.pages.customer_page import CustomerPage


class AccountPageLocators:
    LOCATOR_TRANSACTIONS_BUTTON = (
        By.XPATH, "/html/body/div/div/div[2]/div/div[3]/button[1]"
    )
    LOCATOR_DEPOSIT_BUTTON = (
        By.XPATH, "/html/body/div/div/div[2]/div/div[3]/button[2]"
    )
    LOCATOR_WITHDRAW_BUTTON = (
        By.XPATH, "/html/body/div/div/div[2]/div/div[3]/button[3]"
    )

    LOCATOR_FORM_BUTTON = (
        By.XPATH, "/html/body/div/div/div[2]/div/div[4]/div/form/button"
    )
    LOCATOR_FORM_INPUT = (
        By.XPATH, "/html/body/div/div/div[2]/div/div[4]/div/form/div/input"
    )

    LOCATOR_BALANCE_ACCOUNT = (
        By.XPATH, "/html/body/div/div/div[2]/div/div[2]/strong[2]"
    )


class TransactionPageLocators:
    LOCATOR_TABLE = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/table")
    LOCATOR_BODY_ROW = (By.CLASS_NAME, "ng-scope")
    LOCATOR_ROW_ATTRIBUTES = (By.CLASS_NAME, "ng-binding")


class AccountPage(BasePage):
    def __init__(self, *args, **kwargs):
        self.url = self.BASE_URL + 'customer'
        super().__init__(*args, **kwargs)

    def go_to_page(self):
        self.driver.get(self.url)
        CustomerPage.login(self.driver, self.wait)
        self.driver.refresh()

    def make_search_transaction(self):
        by, value = AccountPageLocators.LOCATOR_TRANSACTIONS_BUTTON

        self.wait.until(ec.presence_of_element_located((by, value)))
        self.driver.find_element(by, value).click()
        self.wait.until(ec.url_contains('listTx'))

        assert self.driver.current_url == self.BASE_URL + 'listTx'

    def make_search_deposit(self):
        by, value = AccountPageLocators.LOCATOR_DEPOSIT_BUTTON

        self.wait.until(ec.element_to_be_clickable((by, value)))
        self.driver.find_element(by, value).click()

        by, value = AccountPageLocators.LOCATOR_FORM_BUTTON

        self.wait.until(ec.element_to_be_clickable((by, value)))
        self.driver.find_element(by, value)

    def make_search_withdraw(self):
        by, value = AccountPageLocators.LOCATOR_WITHDRAW_BUTTON

        self.wait.until(ec.element_to_be_clickable((by, value)))
        self.driver.find_element(by, value).click()

        by, value = AccountPageLocators.LOCATOR_FORM_BUTTON

        self.wait.until(ec.element_to_be_clickable((by, value)))
        self.driver.find_element(by, value)

    def deposit(self, n: int):
        self.driver.refresh()
        self.make_search_deposit()

        by, value = AccountPageLocators.LOCATOR_FORM_INPUT
        self.driver.find_element(by, value).send_keys(n)

        by, value = AccountPageLocators.LOCATOR_FORM_BUTTON
        self.driver.find_element(by, value).click()

    def withdraw(self, n: int):
        self.driver.refresh()
        self.make_search_withdraw()

        by, value = AccountPageLocators.LOCATOR_FORM_INPUT
        self.driver.find_element(by, value).send_keys(n)

        by, value = AccountPageLocators.LOCATOR_FORM_BUTTON
        self.driver.find_element(by, value).click()

    def check_transactions(self) -> list:
        self.driver.refresh()

        by, value = AccountPageLocators.LOCATOR_BALANCE_ACCOUNT
        self.wait.until(ec.presence_of_element_located((by, value)))
        element = self.driver.find_element(by, value)

        assert int(element.text) == 0

        self.make_search_transaction()

        by, value = TransactionPageLocators.LOCATOR_TABLE
        self.wait.until(ec.presence_of_element_located((by, value)))
        element = self.driver.find_element(by, value)

        by, value = TransactionPageLocators.LOCATOR_BODY_ROW
        transactions = element.find_elements(by, value)

        transaction_list = []

        for transaction in transactions:
            by, value = TransactionPageLocators.LOCATOR_ROW_ATTRIBUTES
            date, amount, tr_type = transaction.find_elements(by, value)

            transaction_list.append((date.text, amount.text, tr_type.text))

        return transaction_list
