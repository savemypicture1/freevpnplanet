import allure
from typing import Tuple
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20, poll_frequency=1)


    def open(self) -> None:
        with allure.step(f'Open {self.PAGE_URL}'):
            self.driver.get(self.PAGE_URL)

    def get_text(self, locator: Tuple[str, str]) -> str:
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def click(self, locator: Tuple[str, str], button_name: str) -> None:
        with allure.step(f'Click on {button_name} button'):
            self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator: Tuple[str, str], field_name: str, text: str) -> None:
        with allure.step(f'Enter {field_name}: {text}'):
            self.wait.until(EC.element_to_be_clickable(locator)).send_keys(text)
