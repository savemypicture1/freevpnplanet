from selenium.webdriver.remote.webelement import WebElement

from pages.cabinet_page import CabinetPage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage(CabinetPage):
    PAGE_URL = Links.PROFILE_PAGE

    LOGOUT = ('css selector', '.title-exit')
    EMAIL = ('css selector', '.user-email b')
    ACCOUNT_STATUS = ('css selector', '.user-account-status__status')
    PLAN = ('css selector', '.details-row b')
    TARIFF_VALIDITY_PERIOD = ('css selector', '.details-col svg')

    CHANGE_PASSWORD_BUTTON = ('css selector', '.buttons-wrap .change-password')
    VERIFY_ACCOUNT_BUTTON = ('css selector', '.sending button')

    HISTORY_TABLE = ('css selector', '.history-table')

    OLD_NEW_CONFIRM_PASSWORD_FIELDS = ('css selector', '.input-field input')
    CONFIRM_CHANGE_PASSWORD_BUTTON = ('css selector', '.changePassword__buttons-wrap button:first-child')
    CLOSE_BUTTON = ('css selector', '.changePassword__buttons-wrap button:last-child')

    PASSWORD_WAS_CHANGED_MSG = ('css selector', '.changePassword__success')

    ERROR_VALIDATION_MSG = ('css selector', '.input-field__error')

    def click_logout(self) -> None:
        self.click(self.LOGOUT)

    def get_email(self) -> str:
        return self.get_text(self.EMAIL)

    def get_account_status(self) -> str:
        return self.get_text(self.ACCOUNT_STATUS)

    def get_tariff_plan(self) -> str:
        return self.get_text(self.PLAN)

    def get_tariff_validity_period(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(self.TARIFF_VALIDITY_PERIOD))

    def verify_account_button_is_visible(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(self.VERIFY_ACCOUNT_BUTTON))

    def verify_account_button_is_not_visible(self) -> WebElement:
        return self.wait.until(EC.invisibility_of_element_located(self.VERIFY_ACCOUNT_BUTTON))

    def click_verify_account_button(self) -> None:
        self.click(self.VERIFY_ACCOUNT_BUTTON)

    def get_history_table_text(self) -> str:
        return self.get_text(self.HISTORY_TABLE)

    def click_change_password_button(self) -> None:
        self.click(self.CHANGE_PASSWORD_BUTTON)

    def get_password_fields(self) -> list[WebElement]:
        return self.wait.until(EC.visibility_of_all_elements_located(self.OLD_NEW_CONFIRM_PASSWORD_FIELDS))

    def enter_change_passwords(self, old_password: str, new_password: str, confirm_password: str):
        password_fields = self.get_password_fields()
        password_fields[0].send_keys(old_password)
        password_fields[1].send_keys(new_password)
        password_fields[2].send_keys(confirm_password)

    def click_confirm_change_password_button(self) -> None:
        self.click(self.CONFIRM_CHANGE_PASSWORD_BUTTON)

    def get_password_was_changed_message(self) -> str:
        return self.get_text(self.PASSWORD_WAS_CHANGED_MSG)

    def get_wrong_old_password_message(self) -> str:
        return self.get_text(self.ERROR_VALIDATION_MSG)
