import pytest
import allure

from src.pages.account_page import AccountPage
from src.pages.login_page import LoginPage
from src.pages.customer_page import CustomerPage
from src.utils import save_csv


@allure.feature('Сценарий авторизации, пополнения,'
                'вывода и просмотра и сверки транзакций')
class TestScenario:
    transactions = []

    @allure.story('Приходим на страницу "Логина"')
    @pytest.mark.page_obj(LoginPage.__name__)
    def test_redirect_to_customer_login(
            self,
            page: LoginPage,
    ):
        with allure.step('Редирект на страницу авторизации пользователя'):
            page.go_to_page()
            page.redirect_to_customer_login()

    @allure.story('Авторизация')
    @pytest.mark.page_obj(CustomerPage.__name__)
    def test_authorization(
            self,
            page: CustomerPage,
            fibonacci_day: int
    ):
        with allure.step('Авторизируемся и переходим на страницу аккаунта'):
            page.make_login()

    @allure.story('Депозит')
    @pytest.mark.page_obj(AccountPage.__name__)
    def test_deposit(
            self,
            page: AccountPage,
            fibonacci_day: int
    ):
        with allure.step('Выполненние операции "депозит"'):
            tr_credit = page.deposit(fibonacci_day)
            self.transactions.append(tr_credit)

    @allure.story('Вывод')
    @pytest.mark.page_obj(AccountPage.__name__)
    def test_withdraw(
            self,
            page: AccountPage,
            fibonacci_day: int
    ):
        with allure.step('Выполнение операции вывода средств'):
            tr_debit = page.withdraw(fibonacci_day)
            self.transactions.append(tr_debit)

    @allure.story('Проверка баланса')
    @pytest.mark.page_obj(AccountPage.__name__)
    def test_account_balance(
            self,
            page: AccountPage,
    ):
        with allure.step('Сверка баланса'):
            account_balance = page.get_account_balance()

            assert account_balance == 0

    @allure.story('Транзакции')
    @pytest.mark.page_obj(AccountPage.__name__)
    def test_check_transactions(
            self,
            page: AccountPage,
    ):
        with allure.step('Просмотр транзакций'):
            transactions = page.check_transactions(
                expected_transactions=self.transactions
            )
            save_csv(data=transactions)
            allure.attach.file(
                'allure-data.csv',
                name='transactions',
                attachment_type=allure.attachment_type.CSV
            )
