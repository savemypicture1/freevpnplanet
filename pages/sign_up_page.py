from pages.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class SignupPage(BasePage):
    PAGE_URL = Links.SIGN_UP_PAGE

    SIGN_UP_TITLE = ('css selector', '.login-slot:nth-child(4) .title')
    EMAIL_FIELD = ('css selector', '.login-slot:nth-child(4) .login-input:nth-child(2) input')
    CREATE_BUTTON = ('css selector', '.login-slot:nth-child(4) button')
    NEXT_BUTTON = ('css selector', '[href="/cabinet/download/?form=signup"]')
    ERROR_MSG = ('css selector', '.login-slot .error-text')

    def get_title(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.SIGN_UP_TITLE)).text

    def enter_email(self, email: str) -> None:
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(email)

    def click_create_button(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.CREATE_BUTTON)).click()

    def click_next_button(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON)).click()

    def get_error_msg(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MSG)).text
