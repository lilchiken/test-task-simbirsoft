import re
from typing import Iterable, Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from src.pages.base_page import BasePage
from src.pages.customer_page import CustomerPage
from src.utils import get_time_now


class AccountPageLocators:
    TRANSACTION_BUTTON = (By.CSS_SELECTOR, "button[ng-click*='transactions']")
    DEPOSIT_BUTTON = (By.CSS_SELECTOR, "button[ng-click*='deposit']")
    WITHDRAW_BUTTON = (By.CSS_SELECTOR, "button[ng-click*='withdrawl']")

    FORM_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORM_INPUT = (By.CSS_SELECTOR, "input[ng-model='amount']")

    ACCOUNT_HEAD = (By.CSS_SELECTOR, "div.center[ng-hide='noAccount']")


class TransactionPageLocators:
    TABLE = (By.CSS_SELECTOR, "table")
    BODY_ROW = (By.CSS_SELECTOR, "tr.ng-scope")
    ROW_ATTRIBUTE = (By.CSS_SELECTOR, "td.ng-binding")


class AccountPage(BasePage):
    def __init__(self, *args, **kwargs):
        self.url = self.BASE_URL + 'customer'
        super().__init__(*args, **kwargs)

    def go_to_page(self):
        self.driver.get(self.url)
        CustomerPage.login(self.driver, self.wait)
        self.driver.refresh()

    def make_search_transaction(self):
        by, value = AccountPageLocators.TRANSACTION_BUTTON

        self.wait.until(ec.presence_of_element_located((by, value)))
        self.driver.find_element(by, value).click()
        self.wait.until(ec.url_contains('listTx'))

        assert self.driver.current_url == self.BASE_URL + 'listTx'

    def make_search_deposit(self):
        by, value = AccountPageLocators.DEPOSIT_BUTTON

        self.wait.until(ec.element_to_be_clickable((by, value)))
        self.driver.find_element(by, value).click()

        by, value = AccountPageLocators.FORM_BUTTON

        self.wait.until(ec.element_to_be_clickable((by, value)))
        self.driver.find_element(by, value)

    def make_search_withdraw(self):
        by, value = AccountPageLocators.WITHDRAW_BUTTON

        self.wait.until(ec.element_to_be_clickable((by, value)))
        self.driver.find_element(by, value).click()

        by, value = AccountPageLocators.FORM_BUTTON

        self.wait.until(ec.element_to_be_clickable((by, value)))
        self.driver.find_element(by, value)

    def deposit(self, n: int):
        self.driver.refresh()
        self.make_search_deposit()

        by, value = AccountPageLocators.FORM_INPUT
        self.driver.find_element(by, value).send_keys(n)

        by, value = AccountPageLocators.FORM_BUTTON
        self.driver.find_element(by, value).click()
        time_now = get_time_now()

        return time_now, str(n), 'Credit'

    def withdraw(self, n: int):
        self.driver.refresh()
        self.make_search_withdraw()

        by, value = AccountPageLocators.FORM_INPUT
        self.driver.find_element(by, value).send_keys(n)

        by, value = AccountPageLocators.FORM_BUTTON
        self.driver.find_element(by, value).click()
        time_now = get_time_now()

        return time_now, str(n), 'Debit'

    def get_account_balance(self) -> int:
        self.driver.refresh()

        by, value = AccountPageLocators.ACCOUNT_HEAD
        self.wait.until(ec.presence_of_element_located((by, value)))
        element = self.driver.find_element(by, value)

        account_head = element.text
        childs = account_head.split(' , ')

        for child in childs:
            if 'Balance' in child:
                child.split(' : ')
                return int(child[-1])

    def check_transactions(
            self,
            expected_transactions: Iterable[Tuple[str, str, str]]
    ) -> list:
        self.driver.refresh()

        by, value = AccountPageLocators.ACCOUNT_HEAD
        self.wait.until(ec.presence_of_element_located((by, value)))
        self.driver.find_element(by, value)

        self.make_search_transaction()

        by, value = TransactionPageLocators.TABLE
        self.wait.until(ec.presence_of_element_located((by, value)))
        element = self.driver.find_element(by, value)

        by, value = TransactionPageLocators.BODY_ROW
        transactions = element.find_elements(by, value)

        transaction_list = []

        for transaction in transactions:
            by, value = TransactionPageLocators.ROW_ATTRIBUTE
            date, amount, tr_type = transaction.find_elements(by, value)

            transaction_list.append((date.text, amount.text, tr_type.text))

        for tr, expected_tr in zip(transaction_list, expected_transactions):
            tr_date, *_ = tr
            expected_tr_date, *_ = expected_tr

            assert re.match(expected_tr_date, tr_date)
            assert tr[1:] == expected_tr[1:]

        return transaction_list
