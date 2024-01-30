from selenium import webdriver

from src.pages.base_page import BasePage
from src.pages.login_page import LoginPage
from src.pages.customer_page import CustomerPage
from src.pages.account_page import AccountPage


__all__ = [
    'DriverConf',
    'Pages'
]


class DriverConf:
    command_executor = "http://localhost:4444"
    options = webdriver.FirefoxOptions()


class Pages:
    BasePage = BasePage
    LoginPage = LoginPage
    CustomerPage = CustomerPage
    AccountPage = AccountPage
