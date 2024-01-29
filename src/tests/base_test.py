from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from selenium.webdriver import Remote
    from selenium.webdriver.support.wait import WebDriverWait


class BaseTest:
    driver: 'Remote'
    wait: 'WebDriverWait'

    @pytest.fixture
    def init_webdriver(self, driver, wait):
        self.driver = driver
        self.driver.delete_all_cookies()

        self.driver.maximize_window()
        self.wait = wait

        yield self.wait, self.driver

        self.driver.quit()
