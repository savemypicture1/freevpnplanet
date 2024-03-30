from pages.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    SIGN_IN_TITLE = ('css selector', '.login-slot:nth-child(2) .title')
    EMAIL_FIELD = ('css selector', '.login-slot:nth-child(2) .login-input:nth-child(2) input')
    PASSWORD_FIELD = ('css selector', '.login-slot:nth-child(2) .login-input:nth-child(3) input')
    LOGIN_BUTTON = ('css selector', '.login-slot:nth-child(2) button')
    SIGN_UP_BUTTON = ('css selector', '[href="/login/?form=signup"]')

    def get_title(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.SIGN_IN_TITLE)).text

    def enter_email(self, email: str) -> None:
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(email)

    def enter_password(self, password: str) -> None:
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    def click_login_button(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def click_sign_up(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.SIGN_UP_BUTTON)).click()
