from pages.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    PAGE_URL = Links.HOST

    LOG_IN_BUTTON = ('css selector', '[href="/login/"]')

    def click_log_in_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOG_IN_BUTTON)).click()
