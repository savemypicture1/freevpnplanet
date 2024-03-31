from typing import Tuple

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self) -> None:
        self.driver.get(self.PAGE_URL)

    def get_text(self, locator: Tuple[str, str]) -> str:
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def click(self, locator: Tuple[str, str]) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator: Tuple[str, str], text: str) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(text)
