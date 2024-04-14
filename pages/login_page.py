from base.base_page import BasePage
from config.links import Links


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    SIGN_IN_TITLE = ('css selector', '.login-slot:nth-child(2) .title')
    EMAIL_FIELD = ('css selector', '.login-slot:nth-child(2) .login-input:nth-child(2) input')
    PASSWORD_FIELD = ('css selector', '.login-slot:nth-child(2) .login-input:nth-child(3) input')
    LOGIN_BUTTON = ('css selector', '.login-slot:nth-child(2) button')
    SIGN_UP_BUTTON = ('css selector', '[href="/login/?form=signup"]')
    ERROR_MSG = ('css selector', '.error-text')

    def get_title(self) -> str:
        return self.get_text(self.SIGN_IN_TITLE)

    def enter_email(self, email: str) -> None:
        self.send_keys(self.EMAIL_FIELD, email)

    def enter_password(self, password: str) -> None:
        self.send_keys(self.PASSWORD_FIELD, password)

    def click_login_button(self) -> None:
        self.click(self.LOGIN_BUTTON)

    def click_sign_up(self) -> None:
        self.click(self.SIGN_UP_BUTTON)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MSG)
