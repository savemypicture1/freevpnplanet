from base.base_page import BasePage
from config.links import Links


class SignupPage(BasePage):
    PAGE_URL = Links.SIGN_UP_PAGE

    SIGN_UP_TITLE = ('css selector', '.login-slot:nth-child(4) .title')
    EMAIL_FIELD = ('css selector', '.login-slot:nth-child(4) .login-input:nth-child(2) input')
    CREATE_BUTTON = ('css selector', '.login-slot:nth-child(4) button')
    NEXT_BUTTON = ('css selector', '[href="/cabinet/download/?form=signup"]')
    ERROR_MSG = ('css selector', '.login-slot .error-text')

    def get_title(self) -> str:
        return self.get_text(self.SIGN_UP_TITLE)

    def enter_email(self, email: str) -> None:
        self.send_keys(self.EMAIL_FIELD, email)

    def click_create_button(self) -> None:
        self.click(self.CREATE_BUTTON)

    def click_next_button(self) -> None:
        self.click(self.NEXT_BUTTON)

    def get_error_msg(self) -> str:
        return self.get_text(self.ERROR_MSG)
