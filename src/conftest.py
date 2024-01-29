import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from src.conf import DriverConf, Pages
from src_lib.fibonacci_day import get_fibonacci_day


@pytest.fixture
def driver(request) -> 'webdriver.Remote':
    driver = webdriver.Remote(
        command_executor=DriverConf.command_executor,
        options=DriverConf.options
    )

    yield driver

    driver.quit()


@pytest.fixture
def wait(driver) -> 'WebDriverWait':
    wait = WebDriverWait(driver, 10)
    return wait


@pytest.fixture
def page(request, driver, wait):
    marker = request.node.get_closest_marker('page_obj')
    arg = marker.args[0]
    page_cls = getattr(Pages, arg)
    page = page_cls(driver, wait)
    return page


@pytest.fixture
def fibonacci_day():
    return get_fibonacci_day()
