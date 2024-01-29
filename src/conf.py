from selenium import webdriver

from src.pages.base_page import BasePage
from src.pages.login_page import LoginPage
from src.pages.customer_page import CustomerPage
from src.pages.account_page import AccountPage


__all__ = [
    'DriverConf',
    'Pages'
]


USER_AGENT = (
    """
    Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0)
    Gecko/20100101 Firefox/122.0
    """
)

options = webdriver.FirefoxOptions()
options.set_preference(
    "general.useragent.override",
    USER_AGENT
)


class DriverConf:
    command_executor = "http://localhost:4444"
    options = webdriver.FirefoxOptions()


class Pages:
    BasePage = BasePage
    LoginPage = LoginPage
    CustomerPage = CustomerPage
    AccountPage = AccountPage
