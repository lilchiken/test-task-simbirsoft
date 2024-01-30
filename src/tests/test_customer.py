import pytest
import allure

from src.pages.customer_page import CustomerPage


@pytest.mark.page_obj(CustomerPage.__name__)
@allure.feature('Customer page')
class TestCustomer:
    @allure.story('Авторизация')
    def test_search(self, page):
        page.go_to_page()
        page.make_search()
