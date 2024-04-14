from base.base_page import BasePage
from config.links import Links


class MainPage(BasePage):
    PAGE_URL = Links.HOST

    LOG_IN_BUTTON = ('css selector', '[href="/login/"]')

    def click_log_in_button(self) -> None:
        self.click(self.LOG_IN_BUTTON)
