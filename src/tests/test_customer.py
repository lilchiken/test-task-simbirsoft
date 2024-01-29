import pytest

from src.pages.customer_page import CustomerPage
from src.tests.base_test import BaseTest


@pytest.mark.page_obj(CustomerPage.__name__)
class TestCustomer(BaseTest):
    def test_search(self, page):
        page.go_to_page()
        page.make_search()
