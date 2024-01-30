import pytest
import allure

from src.pages.login_page import LoginPage


@pytest.mark.page_obj(LoginPage.__name__)
@allure.feature('Login page')
class TestLogin:
    @allure.story('Логин')
    def test_search(self, page):
        page.go_to_page()
        page.make_search()
