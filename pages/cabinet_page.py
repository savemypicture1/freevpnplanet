from pages.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CabinetPage(BasePage):
    PROFILE = ('css selector', '[href="/cabinet/?page=profile"]')
    DOWNLOAD = ('css selector', '[href="/cabinet/download/"]')
    CONFIGURATIONS = ('css selector', '[href="/cabinet/configuration/"]')

    def get_title(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.TITLE)).text

    def click_profile_button(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.PROFILE)).click()
