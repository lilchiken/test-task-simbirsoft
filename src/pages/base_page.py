from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from selenium.webdriver import Remote
    from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    BASE_URL = (
        "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/"
    )

    def __init__(
            self,
            driver: 'Remote',
            wait: 'WebDriverWait'
    ) -> None:
        self.driver = driver
        self.wait = wait

    def goto(self, url: str):
        self.driver.get(url)
