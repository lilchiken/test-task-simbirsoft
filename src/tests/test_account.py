import pytest
import allure

from src.pages.account_page import AccountPage
from src.utils import save_csv


@pytest.mark.page_obj(AccountPage.__name__)
@allure.feature('Account page')
class TestAccount:

    @allure.story('Транзакция')
    def test_search_transaction(self, page):
        page.go_to_page()
        page.make_search_transaction()

    @allure.story('Депозит')
    def test_search_deposit(self, page):
        page.go_to_page()
        page.make_search_deposit()

    @allure.story('Вывод')
    def test_search_withdraw(self, page):
        page.go_to_page()
        page.make_search_withdraw()

    @allure.story('Сценарий пополнения, вывода и просмотра транзакций')
    def test_scenario(self, page, fibonacci_day):
        with allure.step('Переход на страницу'):
            page.go_to_page()
        with allure.step('Депозит'):
            page.deposit(fibonacci_day)
        with allure.step('Вывод'):
            page.withdraw(fibonacci_day)
        with allure.step('Просмотр транзакций'):
            transactions = page.check_transactions()
            save_csv(data=transactions)
            allure.attach.file(
                'allure-data.csv',
                name='transactions',
                attachment_type=allure.attachment_type.CSV
            )
