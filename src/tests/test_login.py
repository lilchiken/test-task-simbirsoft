import pytest

from src.pages.login_page import LoginPage
from src.tests.base_test import BaseTest


@pytest.mark.page_obj(LoginPage.__name__)
class TestLogin(BaseTest):
    def test_search(self, page):
        page.go_to_page()
        page.make_search()
