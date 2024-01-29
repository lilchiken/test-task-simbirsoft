import pytest
import allure

from src.pages.login_page import LoginPage
from src.tests.base_test import BaseTest


@pytest.mark.page_obj(LoginPage.__name__)
@allure.feature('Login page')
class TestLogin(BaseTest):
    @allure.story('Логин')
    def test_search(self, page):
        page.go_to_page()
        page.make_search()
